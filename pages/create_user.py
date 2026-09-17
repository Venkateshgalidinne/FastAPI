import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("📝 Create Account")

with st.form("Create_user"):

    name = st.text_input(
        "Name",
        placeholder="Enter your name"
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

    role = st.selectbox(
        "Choose Role",
        ["Recruiter", "Jobseeker"]
    )

    create_account = st.form_submit_button(
        "Create Account"
    )


if create_account:

    # Check empty fields
    if name == "":
        st.error("Please enter your name.")

    elif email == "":
        st.error("Please enter your email.")

    elif password == "":
        st.error("Please enter your password.")

    elif confirm_password == "":
        st.error("Please confirm your password.")

    # Check password
    elif password != confirm_password:
        st.error("Passwords do not match.")

    else:

        new_user = {
            "name": name,
            "email": email,
            "password": password,
            "role": role
        }

        try:

            response = requests.post(
                API_URL + "/create_user",
                json=new_user
            )

            if response.status_code == 200:

                data = response.json()

                if data["msg"] == "Email already exists":

                    st.error("Email already exists.")

                else:

                    st.success(
                        "✅ Account created successfully!"
                    )

                    # Store selected role
                    st.session_state["selected_role"] = role

                    # Go directly to correct login page
                    if role == "Recruiter":

                        st.switch_page(
                            "pages/recruiter.py"
                        )

                    elif role == "Jobseeker":

                        st.switch_page(
                            "pages/jobseeker.py"
                        )

            else:

                st.error(
                    "Something went wrong while creating account."
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Cannot connect to FastAPI. "
                "Please start the backend server."
            )