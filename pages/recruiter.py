import streamlit as st
import requests
from api_config import API_URL

API_URL = "http://127.0.0.1:8000"


# =====================================================
# SESSION STATE
# =====================================================

if "recruiter_logged_in" not in st.session_state:
    st.session_state["recruiter_logged_in"] = False

if "recruiter_name" not in st.session_state:
    st.session_state["recruiter_name"] = ""

if "recruiter_email" not in st.session_state:
    st.session_state["recruiter_email"] = ""


# =====================================================
# TITLE
# =====================================================

st.title("👨‍💼 Recruiter")


# =====================================================
# RECRUITER LOGIN
# =====================================================

if st.session_state["recruiter_logged_in"] == False:

    st.subheader("🔐 Recruiter Login")

    email = st.text_input(
        "Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        login_data = {
            "email": email,
            "password": password
        }

        try:

            response = requests.post(
                API_URL + "/login",
                json=login_data
            )

            if response.status_code == 200:

                data = response.json()

                # Login successful
                if data["login"] == True:

                    # Check recruiter role
                    if data["role"] == "Recruiter":

                        st.session_state["recruiter_logged_in"] = True

                        st.session_state["recruiter_name"] = data["name"]

                        st.session_state["recruiter_email"] = data["email"]

                        st.success(
                            "Login successful!"
                        )

                        st.rerun()

                    else:

                        st.error(
                            "This account is not a Recruiter."
                        )

                else:

                    st.error(
                        data["msg"]
                    )

            else:

                st.error(
                    f"Login failed. Status Code: {response.status_code}"
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "Cannot connect to FastAPI. "
                "Please start the backend server."
            )


# =====================================================
# RECRUITER DASHBOARD
# =====================================================

else:

    st.success(
        f"Welcome {st.session_state['recruiter_name']} 👋"
    )

    st.write(
        "Email:",
        st.session_state["recruiter_email"]
    )


    # =================================================
    # LOGOUT
    # =================================================

    if st.button("Logout"):

        st.session_state["recruiter_logged_in"] = False

        st.session_state["recruiter_name"] = ""

        st.session_state["recruiter_email"] = ""

        st.rerun()


    st.divider()


    # =================================================
    # POST JOB
    # =================================================

    st.subheader("📢 Post a New Job")


    with st.form("job_form"):

        title = st.text_input(
            "Job Title",
            placeholder="Python Developer"
        )

        company = st.text_input(
            "Company Name",
            placeholder="ABC Technologies"
        )

        location = st.text_input(
            "Location",
            placeholder="Hyderabad"
        )

        salary = st.text_input(
            "Salary",
            placeholder="5 - 8 LPA"
        )

        experience = st.text_input(
            "Experience",
            placeholder="0 - 2 Years"
        )

        description = st.text_area(
            "Job Description"
        )

        apply_url = st.text_input(
            "Company Careers / Apply URL",
            placeholder="https://company.com/careers"
        )


        post_job = st.form_submit_button(
            "🚀 Post Job"
        )


        if post_job:

            if title == "":
                st.error("Please enter Job Title.")

            elif company == "":
                st.error("Please enter Company Name.")

            elif location == "":
                st.error("Please enter Location.")

            elif apply_url == "":
                st.error("Please enter Company Careers URL.")

            else:

                new_job = {

                    "title": title,

                    "company": company,

                    "location": location,

                    "salary": salary,

                    "experience": experience,

                    "description": description,

                    "recruiter_email":
                        st.session_state[
                            "recruiter_email"
                        ],

                    "apply_url": apply_url
                }


                try:

                    response = requests.post(
                        API_URL + "/create_job",
                        json=new_job
                    )


                    if response.status_code == 200:

                        data = response.json()

                        st.success(
                            "✅ Job posted successfully!"
                        )

                    else:

                        st.error(
                            "Failed to post job."
                        )


                except requests.exceptions.ConnectionError:

                    st.error(
                        "Cannot connect to FastAPI."
                    )


    st.divider()


    # =================================================
    # MY POSTED JOBS
    # =================================================

    st.subheader("📋 My Posted Jobs")


    try:

        response = requests.get(
            API_URL + "/recruiter/jobs",
            params={
                "email":
                    st.session_state[
                        "recruiter_email"
                    ]
            }
        )


        if response.status_code == 200:

            my_jobs = response.json()


            if len(my_jobs) == 0:

                st.info(
                    "You have not posted any jobs yet."
                )


            else:

                for job in my_jobs:

                    st.markdown("---")

                    st.subheader(
                        f"💼 {job['title']}"
                    )

                    st.write(
                        f"🏢 Company: {job['company']}"
                    )

                    st.write(
                        f"📍 Location: {job['location']}"
                    )

                    st.write(
                        f"💰 Salary: {job['salary']}"
                    )

                    st.write(
                        f"🧑‍💼 Experience: {job['experience']}"
                    )

                    st.write(
                        f"📝 Description: {job['description']}"
                    )

                    st.link_button(
                        "🔗 Company Careers",
                        job["apply_url"]
                    )


        else:

            st.error(
                "Unable to load your jobs."
            )


    except requests.exceptions.ConnectionError:

        st.error(
            "Cannot connect to FastAPI."
        )