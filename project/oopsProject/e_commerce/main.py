import streamlit as st


st.set_page_config(
    page_title="OOP E-Commerce",
    page_icon="🛒",
    layout="wide"
)


# =====================================
# SESSION STATE
# =====================================

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False


if "user" not in st.session_state:

    st.session_state.user = None


if "cart" not in st.session_state:

    st.session_state.cart = None


# =====================================
# HOME PAGE
# =====================================

st.title("🛒 OOP E-Commerce Store")

st.subheader(
    "Python OOP + Streamlit + JSON"
)

st.write(
    """
    Welcome to our E-Commerce project! 👋
    """
)

col1, col2, col3 = st.columns(3)

with col1:

    st.info(
        "👤 User Management"
    )

with col2:

    st.info(
        "🛍️ Product Management"
    )

with col3:

    st.info(
        "📦 Order Management"
    )


st.divider()

st.markdown(
    """
    ### 🧱 OOP Concepts Used

    - Class
    - Object
    - Constructor
    - Encapsulation
    - Inheritance
    - Polymorphism

    ### 🛠️ Technologies

    - Python
    - Streamlit
    - JSON
    """
)

if not st.session_state.logged_in:

    st.warning(
        "Please use the Login page from the sidebar."
    )

else:

    st.success(
        f"Welcome {st.session_state.user.name}! 👋"
    )

    st.write(
        f"Role: **{st.session_state.user.role}**"
    )