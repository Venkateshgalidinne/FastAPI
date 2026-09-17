import streamlit as st
import json


def register_user():

    st.title("📝 Create Account")

    name = st.text_input("Full Name")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    role = st.selectbox(
        "Select Role",
        [
            "Customer",
            "Admin"
        ]
    )

    if st.button("Register"):

        if not name or not email or not password:

            st.error("Please fill all fields.")

            return

        if password != confirm_password:

            st.error("Passwords do not match.")

            return

        try:

            with open("users.json", "r") as file:

                users = json.load(file)

        except FileNotFoundError:

            users = []

        for user in users:

            if user["email"] == email:

                st.error("Email already registered.")

                return

        new_id = len(users) + 1

        new_user = {
            "id": new_id,
            "name": name,
            "email": email,
            "password": password,
            "role": role.lower()
        }

        users.append(new_user)

        with open("users.json", "w") as file:

            json.dump(
                users,
                file,
                indent=4
            )

        st.success(
            "Registration successful! Please login."
        )


register_user()