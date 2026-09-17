import streamlit as st
import json
import os


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Job Seeker Dashboard",
    page_icon="👨‍💼",
    layout="wide"
)


# =========================================================
# LOGIN PROTECTION
# =========================================================

if "loggedin_user" not in st.session_state:

    st.warning("⚠️ Please login first.")

    st.switch_page("pages/login.py")

    st.stop()


# Get logged-in user
user = st.session_state["loggedin_user"]


# =========================================================
# ROLE PROTECTION
# =========================================================

if user["role"] != "Job Seeker":

    st.error(
        "❌ You are not authorized to access the Job Seeker Dashboard."
    )

    st.stop()


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("📋 Menu")

st.sidebar.divider()

st.sidebar.write("### 👤 Job Seeker")

st.sidebar.write(
    f"**Name:** {user['name']}"
)

st.sidebar.write(
    f"**Email:** {user['email']}"
)

st.sidebar.divider()


# Logout
if st.sidebar.button(
    "🚪 Logout",
    use_container_width=True
):

    st.session_state.clear()

    st.switch_page("app.py")


# =========================================================
# LOAD JOBS
# =========================================================

if not os.path.exists("jobs.json"):

    with open("jobs.json", "w") as file:
        json.dump([], file)


with open("jobs.json", "r") as file:

    all_jobs = json.load(file)


# =========================================================
# HEADER
# =========================================================

st.title("👨‍💼 Job Seeker Dashboard")

st.success(
    f"Welcome, {user['name']}! 👋"
)

st.write(
    "Find your dream job and apply directly through the company."
)

st.divider()


# =========================================================
# STATISTICS
# =========================================================

col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "💼 Available Jobs",
        len(all_jobs)
    )


with col2:

    st.metric(
        "🏢 Companies",
        len(set(job["company"] for job in all_jobs))
        if all_jobs else 0
    )


with col3:

    st.metric(
        "🚀 Applications",
        "0"
    )


st.divider()


# =========================================================
# SEARCH AND FILTER
# =========================================================

st.subheader("🔎 Find Your Dream Job")


col1, col2 = st.columns(2)


with col1:

    search = st.text_input(
        "Search Job",
        placeholder="Example: Python Developer"
    )


with col2:

    locations = ["All Locations"]

    locations.extend(
        sorted(
            set(
                job["location"]
                for job in all_jobs
            )
        )
    )

    selected_location = st.selectbox(
        "📍 Location",
        locations
    )


# =========================================================
# FILTER JOBS
# =========================================================

filtered_jobs = []


for job in all_jobs:

    # Search condition
    search_match = (
        search.lower() in job["job_title"].lower()
        or search.lower() in job["company"].lower()
        or search.lower() in job["skills"].lower()
    )

    # Location condition
    location_match = (
        selected_location == "All Locations"
        or job["location"] == selected_location
    )

    if search_match and location_match:

        filtered_jobs.append(job)


st.divider()


# =========================================================
# DISPLAY JOBS
# =========================================================

st.subheader(
    f"💼 Available Jobs ({len(filtered_jobs)})"
)


if len(filtered_jobs) == 0:

    st.info(
        "📭 No jobs found. Try another search."
    )


else:

    for job in reversed(filtered_jobs):

        with st.container(border=True):

            # -----------------------------
            # JOB TITLE
            # -----------------------------

            st.subheader(
                f"💼 {job['job_title']}"
            )

            st.write(
                f"🏢 **{job['company']}**"
            )


            # -----------------------------
            # JOB INFORMATION
            # -----------------------------

            col1, col2, col3 = st.columns(3)


            with col1:

                st.write(
                    f"📍 **Location:** {job['location']}"
                )


            with col2:

                st.write(
                    f"💰 **Salary:** {job['salary']}"
                )


            with col3:

                st.write(
                    f"🕒 **Job Type:** {job['job_type']}"
                )


            st.write(
                f"🎯 **Experience:** {job['experience']}"
            )


            st.write(
                f"🛠️ **Skills:** {job['skills']}"
            )


            # -----------------------------
            # DESCRIPTION
            # -----------------------------

            with st.expander("📖 View Job Description"):

                st.write(
                    job["description"]
                )


            # -----------------------------
            # APPLY BUTTON
            # -----------------------------

            st.link_button(
                "🚀 Apply Now",
                job["application_url"],
                use_container_width=True
            )


            st.caption(
                f"Posted by {job['recruiter_name']} "
                f"on {job['created_at']}"
            )