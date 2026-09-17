import streamlit as st
import json

from product import Product


def admin_dashboard():

    st.title("👨‍💼 Admin Dashboard")

    st.subheader("➕ Add Product")

    name = st.text_input(
        "Product Name"
    )

    price = st.number_input(
        "Price",
        min_value=0
    )

    category = st.text_input(
        "Category"
    )

    stock = st.number_input(
        "Stock",
        min_value=0
    )

    if st.button("Add Product"):

        if not name or not category:

            st.error(
                "Please enter product details."
            )

            return

        try:

            with open("products.json", "r") as file:

                products = json.load(file)

        except FileNotFoundError:

            products = []

        product_id = len(products) + 1

        product = Product(
            product_id,
            name,
            price,
            category,
            stock
        )

        products.append(
            product.display_product()
        )

        with open(
            "products.json",
            "w"
        ) as file:

            json.dump(
                products,
                file,
                indent=4
            )

        st.success(
            "Product added successfully!"
        )


admin_dashboard()