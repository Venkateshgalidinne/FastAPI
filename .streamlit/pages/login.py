# import streamlit as st
# import json
# st.title("Login Form")
# with st.form("login_form"):


#     e = st.text_input("Email",Placeholder="Enter your email")
#     p = st.text_input("Password",type="password",placeholder="Enter your password")
#     r = st.radio("Select Role",["Job Seeker","Recruiter"])
#     btn = st.form_submit_button("Login")

#     if btn:
#         with open("users.json","r") as r_file:
#             all_users = json.load(r_file)

#             for user in all_users:
#                 if user["email"] == e and user["password"] == p:
#                     if r == "Recruiter":
#                         st.session_state["Loggedin_user"] = {"email":e,"password":p,"role":"r"}
#                         st.success("loggin as recuriter sucessfully and navgiating towards to the recuriter")
#                         st.switch_page("pages/RecriuterDashboard.py")
#                         break
#                     if r == "jobseeker":
#                         st.session_state["Loggedin_user"] = {"email":e,"password":p,"role":"j"}
#                         st.success("loggin as jobseeker sucessfully and navgiating towards to the jobseeker")
#                         st.switch_page("pages/jobseekerDashboard.py")
#                         break
#                     st.error("user not found  with that credentials")



import streamlit as st
import json
import os

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Login")
st.write("Login to access your Job Portal dashboard.")

st.divider()

with st.form("login_form"):

    email = st.text_input(
        "Email",
        placeholder="Enter your email"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password"
    )

    role = st.radio(
        "Select Role",
        ["Job Seeker", "Recruiter"]
    )

    login_button = st.form_submit_button(
        "Login",
        use_container_width=True
    )


if login_button:

    # Check users.json
    if not os.path.exists("users.json"):

        st.error("No users registered yet.")
        st.stop()

    # Read users
    with open("users.json", "r") as file:
        users = json.load(file)

    logged_in_user = None

    # Check credentials
    for user in users:

        if (
            user["email"].lower() == email.lower()
            and user["password"] == password
            and user["role"] == role
        ):
            logged_in_user = user
            break

    # Login successful
    if logged_in_user:

        # Store user information
        st.session_state["loggedin_user"] = {
            "name": logged_in_user["name"],
            "email": logged_in_user["email"],
            "role": logged_in_user["role"]
        }

        st.success("✅ Login successful!")

        # Navigate according to role
        if role == "Job Seeker":

            st.switch_page("pages/jobseekerDashboard.py")

        elif role == "Recruiter":

            st.switch_page("pages/recruiterDashboard.py")

    else:

        st.error(
            "❌ Invalid email, password, or role."
        )