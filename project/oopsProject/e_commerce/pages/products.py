import streamlit as st
import json

from product import Product


def show_products():

    st.title("🛍️ Products")

    try:

        with open("products.json", "r") as file:

            products = json.load(file)

    except FileNotFoundError:

        st.error("Products file not found.")

        return

    for data in products:

        product = Product(
            data["id"],
            data["name"],
            data["price"],
            data["category"],
            data["stock"]
        )

        st.subheader(
            f"🛒 {product.name}"
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.write(
                f"**Category:** {product.category}"
            )

        with col2:

            st.write(
                f"**Price:** ₹{product.price}"
            )

        with col3:

            st.write(
                f"**Stock:** {product.stock}"
            )

        with col4:

            quantity = st.number_input(
                "Quantity",
                min_value=1,
                max_value=max(1, product.stock),
                value=1,
                key=f"quantity_{product.product_id}"
            )

            if st.button(
                "Add to Cart",
                key=f"add_{product.product_id}"
            ):

                if st.session_state.cart.add_product(
                    product,
                    quantity
                ):

                    st.success(
                        f"{product.name} added to cart!"
                    )

                else:

                    st.error(
                        "Not enough stock."
                    )

        st.divider()


show_products()