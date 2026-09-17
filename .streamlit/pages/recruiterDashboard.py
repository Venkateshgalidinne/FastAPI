import streamlit as st
import json
import os
from datetime import datetime


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Recruiter Dashboard",
    page_icon="🏢",
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

if user["role"] != "Recruiter":

    st.error(
        "❌ You are not authorized to access the Recruiter Dashboard."
    )

    st.stop()


# =========================================================
# CREATE jobs.json IF IT DOES NOT EXIST
# =========================================================

if not os.path.exists("jobs.json"):

    with open("jobs.json", "w") as file:
        json.dump([], file)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("📋 Menu")

st.sidebar.divider()

st.sidebar.write("### 👤 Recruiter")

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
# DASHBOARD HEADER
# =========================================================

st.title("🏢 Recruiter Dashboard")

st.success(
    f"Welcome, {user['name']}! 👋"
)

st.write(
    "Create and manage your job postings from here."
)

st.divider()


# =========================================================
# DASHBOARD STATISTICS
# =========================================================

with open("jobs.json", "r") as file:

    all_jobs = json.load(file)


# Get jobs posted by current recruiter
my_jobs = []

for job in all_jobs:

    if job["recruiter_email"] == user["email"]:

        my_jobs.append(job)


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "💼 My Jobs",
        len(my_jobs)
    )


with col2:

    st.metric(
        "📢 Total Jobs",
        len(all_jobs)
    )


with col3:

    st.metric(
        "📄 Applications",
        "0"
    )


st.divider()


# =========================================================
# CREATE JOB
# =========================================================

st.subheader("➕ Create a New Job")

with st.form("create_job_form"):

    job_title = st.text_input(
        "Job Title",
        placeholder="Example: Python Developer"
    )

    company = st.text_input(
        "Company Name",
        placeholder="Example: ABC Technologies"
    )

    location = st.text_input(
        "Location",
        placeholder="Example: Hyderabad / Remote"
    )

    salary = st.text_input(
        "Salary",
        placeholder="Example: ₹5 - ₹8 LPA"
    )

    skills = st.text_input(
        "Required Skills",
        placeholder="Example: Python, SQL, FastAPI, Git"
    )

    job_type = st.selectbox(
        "Job Type",
        [
            "Full Time",
            "Part Time",
            "Internship",
            "Contract"
        ]
    )

    experience = st.selectbox(
        "Experience",
        [
            "Fresher",
            "0-1 Years",
            "1-3 Years",
            "3-5 Years",
            "5+ Years"
        ]
    )

    description = st.text_area(
        "Job Description",
        placeholder="Enter the complete job description..."
    )

    application_url = st.text_input(
        "Company Careers / Application URL",
        placeholder="https://company.com/careers"
    )

    create_button = st.form_submit_button(
        "🚀 Post Job",
        use_container_width=True
    )


# =========================================================
# SAVE JOB
# =========================================================

if create_button:

    # -----------------------------
    # VALIDATION
    # -----------------------------

    if not job_title.strip():

        st.error("❌ Please enter the job title.")

    elif not company.strip():

        st.error("❌ Please enter the company name.")

    elif not location.strip():

        st.error("❌ Please enter the location.")

    elif not salary.strip():

        st.error("❌ Please enter the salary.")

    elif not skills.strip():

        st.error("❌ Please enter the required skills.")

    elif not description.strip():

        st.error("❌ Please enter the job description.")

    elif not application_url.strip():

        st.error(
            "❌ Please enter the company application URL."
        )

    else:

        # -----------------------------
        # READ EXISTING JOBS
        # -----------------------------

        with open("jobs.json", "r") as file:

            all_jobs = json.load(file)


        # -----------------------------
        # CREATE JOB
        # -----------------------------

        new_job = {

            "job_id": len(all_jobs) + 1,

            "job_title": job_title.strip(),

            "company": company.strip(),

            "location": location.strip(),

            "salary": salary.strip(),

            "skills": skills.strip(),

            "job_type": job_type,

            "experience": experience,

            "description": description.strip(),

            "application_url": application_url.strip(),

            "recruiter_name": user["name"],

            "recruiter_email": user["email"],

            "created_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }


        # -----------------------------
        # ADD JOB
        # -----------------------------

        all_jobs.append(new_job)


        # -----------------------------
        # SAVE TO jobs.json
        # -----------------------------

        with open("jobs.json", "w") as file:

            json.dump(
                all_jobs,
                file,
                indent=4
            )


        st.success(
            "🎉 Job posted successfully!"
        )

        st.balloons()


# =========================================================
# MY JOBS
# =========================================================

st.divider()

st.subheader("📋 My Posted Jobs")


# Reload jobs
with open("jobs.json", "r") as file:

    all_jobs = json.load(file)


# Filter recruiter's jobs
my_jobs = []

for job in all_jobs:

    if job["recruiter_email"] == user["email"]:

        my_jobs.append(job)


# Display jobs

if len(my_jobs) == 0:

    st.info(
        "📭 You haven't posted any jobs yet."
    )

else:

    for job in reversed(my_jobs):

        with st.container(border=True):

            st.subheader(
                f"💼 {job['job_title']}"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.write(
                    f"🏢 **Company:** {job['company']}"
                )

            with col2:

                st.write(
                    f"📍 **Location:** {job['location']}"
                )

            with col3:

                st.write(
                    f"💰 **Salary:** {job['salary']}"
                )


            st.write(
                f"🛠️ **Skills:** {job['skills']}"
            )

            st.write(
                f"📌 **Job Type:** {job['job_type']}"
            )

            st.write(
                f"🎯 **Experience:** {job['experience']}"
            )

            st.write(
                f"📝 **Description:** {job['description']}"
            )

            st.write(
                f"📅 **Posted:** {job['created_at']}"
            )

            st.link_button(
                "🔗 Application Page",
                job["application_url"]
            )