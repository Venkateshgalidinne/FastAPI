
# import streamlit as st
# import json

# st.title("Register Form")
# with st.form("Register_form"):
#    n = st.text_input("Name",placeholder = "Enter your name")
#    e = st.text_input("Email",placeholder = "Enter your email")
#    p = st.text_input("Password",type="password",placeholder = "Enter your password")
#    c_p = st.text_input("confirm Password",type="password",placeholder = "Enter your confirm password")
#    r = st.radio("Select Role",["Job Seeker","Recruiter"])
#    btn = st.form_submit_button("Register")

#    if btn:
#       new_user = {
#             "name":n,
#             "email":e,
#             "password":p,
#             "confirm_password":c_p,
#             "role":r
#       }
#       with open("users.json","r") as r_file:
#          all_users = json.load(r_file)
#          all_users.append(new_user)

#          with open ("users.json","w") as w_file:
#             json.dump(all_users,w_file)

#             st.success("user registered successfully")
#             st.info("please login to access the dashboard")

#             st.switch_page("pages/login.py")


import streamlit as st
import json
import os

st.set_page_config(
    page_title="Register",
    page_icon="📝",
    layout="centered"
)

st.title("📝 Create Your Account")
st.write("Register to access the Job Portal.")

st.divider()

with st.form("register_form"):

    name = st.text_input(
        "Full Name",
        placeholder="Enter your full name"
    )

    email = st.text_input(
        "Email",
        placeholder="Enter your email"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password",
        placeholder="Re-enter your password"
    )

    role = st.radio(
        "Select Role",
        ["Job Seeker", "Recruiter"]
    )

    register_button = st.form_submit_button(
        "Register",
        use_container_width=True
    )


if register_button:

    # Validation
    if not name.strip():
        st.error("Please enter your name.")

    elif not email.strip():
        st.error("Please enter your email.")

    elif not password:
        st.error("Please enter a password.")

    elif password != confirm_password:
        st.error("Passwords do not match.")

    else:

        # Create users.json if it doesn't exist
        if not os.path.exists("users.json"):
            with open("users.json", "w") as file:
                json.dump([], file)

        # Read existing users
        with open("users.json", "r") as file:
            users = json.load(file)

        # Check duplicate email
        email_exists = False

        for user in users:
            if user["email"].lower() == email.lower():
                email_exists = True
                break

        if email_exists:

            st.error("An account with this email already exists.")

        else:

            # Create new user
            new_user = {
                "name": name.strip(),
                "email": email.strip().lower(),
                "password": password,
                "role": role
            }

            users.append(new_user)

            # Save user
            with open("users.json", "w") as file:
                json.dump(users, file, indent=4)

            st.success("✅ Registration successful!")
            st.info("Please login to access your dashboard.")

            st.switch_page("pages/login.py")