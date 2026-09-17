import streamlit as st
import json

from user import Customer, Admin
from cart import Cart


def login_user():

    st.title("🔐 Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        try:

            with open("users.json", "r") as file:

                users = json.load(file)

        except FileNotFoundError:

            st.error("Users file not found.")

            return

        for user in users:

            if (
                user["email"] == email
                and user["password"] == password
            ):

                if user["role"] == "admin":

                    current_user = Admin(
                        user["id"],
                        user["name"],
                        user["email"],
                        user["password"],
                        user["role"]
                    )

                else:

                    current_user = Customer(
                        user["id"],
                        user["name"],
                        user["email"],
                        user["password"],
                        user["role"]
                    )

                st.session_state.user = current_user
                st.session_state.logged_in = True

                st.session_state.cart = Cart(
                    user["id"]
                )

                st.success(
                    "Login successful!"
                )

                st.rerun()

        st.error(
            "Invalid email or password."
        )


login_user()