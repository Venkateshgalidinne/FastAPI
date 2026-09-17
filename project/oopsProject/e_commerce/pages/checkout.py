import streamlit as st
import json

from order import Order


def checkout():

    st.title("💳 Checkout")

    cart = st.session_state.cart

    if not cart.items:

        st.warning("Your cart is empty.")

        return

    st.subheader("Order Summary")

    for item in cart.items:

        st.write(
            f"{item['name']} "
            f"x {item['quantity']} "
            f"= ₹{item['price'] * item['quantity']}"
        )

    total = cart.calculate_total()

    st.divider()

    st.subheader(
        f"Total: ₹{total}"
    )

    address = st.text_area(
        "Delivery Address"
    )

    payment = st.selectbox(
        "Payment Method",
        [
            "Cash on Delivery",
            "UPI",
            "Card"
        ]
    )

    if st.button("Confirm Order"):

        if not address:

            st.error(
                "Please enter delivery address."
            )

            return

        try:

            with open(
                "orders.json",
                "r"
            ) as file:

                orders = json.load(file)

        except FileNotFoundError:

            orders = []

        order_id = len(orders) + 1

        order = Order(
            order_id,
            st.session_state.user.user_id,
            cart.items.copy(),
            total
        )

        order_data = order.get_order_details()

        order_data["address"] = address
        order_data["payment"] = payment

        orders.append(order_data)

        with open(
            "orders.json",
            "w"
        ) as file:

            json.dump(
                orders,
                file,
                indent=4
            )

        cart.clear_cart()

        st.success(
            f"🎉 Order #{order_id} placed successfully!"
        )


checkout()