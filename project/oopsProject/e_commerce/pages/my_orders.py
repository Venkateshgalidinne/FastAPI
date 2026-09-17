import streamlit as st
import json


def show_orders():

    st.title("📦 My Orders")

    try:

        with open("orders.json", "r") as file:

            orders = json.load(file)

    except FileNotFoundError:

        orders = []

    user_id = st.session_state.user.user_id

    my_orders = [
        order
        for order in orders
        if order["user_id"] == user_id
    ]

    if not my_orders:

        st.info("You have no orders yet.")

        return

    for order in my_orders:

        st.subheader(
            f"Order #{order['order_id']}"
        )

        st.write(
            f"Total: ₹{order['total']}"
        )

        st.write(
            f"Status: {order['status']}"
        )

        st.divider()


show_orders()