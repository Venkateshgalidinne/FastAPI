import streamlit as st
import requests
from api_config import API_URL

API_URL = "https://fastapi-jpk3.onrender.com"


# =========================
# JOB SEEKER LOGIN
# =========================

st.title("👨‍💻 Job Seeker")

if "jobseeker_logged_in" not in st.session_state:
    st.session_state["jobseeker_logged_in"] = False


# ---------- LOGIN ----------
if st.session_state["jobseeker_logged_in"] == False:

    st.subheader("🔐 Job Seeker Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        login_data = {

            "email": email,

            "password": password
        }

        response = requests.post(
            API_URL + "/login",
            json=login_data
        )

        if response.status_code == 200:

            data = response.json()

            if data["login"] == True:

                if data["role"] == "JobSeeker":

                    st.session_state["jobseeker_logged_in"] = True

                    st.session_state["jobseeker_name"] = data["name"]

                    st.session_state["jobseeker_email"] = data["email"]

                    st.success(
                        "Login successful!"
                    )

                    st.rerun()

                else:

                    st.error(
                        "This account is not a Job Seeker."
                    )

            else:

                st.error(data["msg"])

        else:

            st.error("Login failed")


# =========================
# JOB SEEKER DASHBOARD
# =========================

else:

    st.success(
        f"Welcome {st.session_state['jobseeker_name']} 👋"
    )

    if st.button("Logout"):

        st.session_state["jobseeker_logged_in"] = False

        st.rerun()

    st.divider()

    # =========================
    # VIEW JOBS
    # =========================

    st.subheader("🔎 Available Jobs")

    response = requests.get(
        API_URL + "/get_all_jobs"
    )

    if response.status_code == 200:

        jobs = response.json()

        if len(jobs) == 0:

            st.info(
                "No jobs available."
            )

        else:

            for job in jobs:

                st.markdown("---")

                st.subheader(
                    f"💼 {job['title']}"
                )

                st.write(
                    f"🏢 **Company:** {job['company']}"
                )

                st.write(
                    f"📍 **Location:** {job['location']}"
                )

                st.write(
                    f"💰 **Salary:** {job['salary']}"
                )

                st.write(
                    f"🧑‍💼 **Experience:** {job['experience']}"
                )

                st.write(
                    f"📝 **Description:** {job['description']}"
                )

                # -------------------------
                # APPLY NOW
                # -------------------------

                st.link_button(
                    "🚀 Apply Now",
                    job["apply_url"]
                )

    else:

        st.error(
            "Unable to load jobs"
        )