import streamlit as st


def show_cart():

    st.title("🛒 My Cart")

    cart = st.session_state.cart

    if not cart.items:

        st.info("Your cart is empty.")

        return

    for item in cart.items:

        col1, col2, col3 = st.columns(3)

        with col1:

            st.write(
                f"**{item['name']}**"
            )

        with col2:

            st.write(
                f"₹{item['price']} × {item['quantity']}"
            )

        with col3:

            if st.button(
                "Remove",
                key=f"remove_{item['product_id']}"
            ):

                cart.remove_product(
                    item["product_id"]
                )

                st.rerun()

    st.divider()

    total = cart.calculate_total()

    st.subheader(
        f"Total Amount: ₹{total}"
    )

    if st.button("Place Order"):

        st.session_state.checkout = True

        st.success(
            "Order ready for checkout!"
        )


show_cart()