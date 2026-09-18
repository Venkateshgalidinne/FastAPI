import streamlit as st
import requests


# ==============================
# TITLE
# ==============================

st.title("🚀 Job Portal")


# ==============================
# USER MANAGEMENT
# ==============================

st.header("User Management")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Create User"):
        st.switch_page("pages/create_user.py")

with col2:
    if st.button("Get Users"):
        response = requests.get("https://fastapi-jpk3.onrender.com" + "/get_all_users")
        

        if response.status_code == 200:
            response_json = response.json()
            st.dataframe(response_json)

with col3:
    if st.button("Delete User"):
        st.switch_page("pages/delete_users.py")

with col4:
    if st.button("Update User"):
        st.switch_page("pages/update_user.py")


# ==============================
# JOB PORTAL
# ==============================

st.header("Job Portal")

col1, col2 = st.columns(2)

with col1:
    if st.button("👨‍💼 Recruiter"):
        st.switch_page("pages/recruiter.py")

with col2:
    if st.button("👨‍💻 Job Seeker"):
        st.switch_page("pages/jobseeker.py")