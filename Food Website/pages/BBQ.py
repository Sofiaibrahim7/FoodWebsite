import streamlit as st

st.set_page_config(page_title="BarBQ Meat", layout="wide")
st.markdown("## 🍖 BarBQ Meat")

# Initialize cart and feedback in session state
if "cart" not in st.session_state:
    st.session_state.cart = {}

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

# ✅ Correct data structure: list of dictionaries
barbq_items = [
    {"img": "images/barbq.png", "name": "BarBQ Classic", "price": 450},
    {"img": "images/bbq.png", "name": "BarBQ Special", "price": 550},
]

# Layout
cols = st.columns(2)

# Display items
for i, item in enumerate(barbq_items):
    with cols[i]:
        st.image(item["img"], width=350)
        st.markdown(f"**{item['name']}**")
        st.markdown(f"Price: Rs {item['price']}")
        if st.button(f"🛒 Add to Cart - {item['name']}"):
            name = item["name"]
            if name in st.session_state.cart:
                st.session_state.cart[name]["quantity"] += 1
            else:
                st.session_state.cart[name] = {"price": item["price"], "quantity": 1}
            st.success(f"{name} added to cart!")

# Description
st.markdown("---")
st.write("Delicious BarBQ meat prepared with our special spices!")

# Cart Section
st.markdown("---")
st.markdown("### 🛒 Your Cart")

if st.session_state.cart:
    total_price = 0
    for name, info in st.session_state.cart.items():
        qty = info["quantity"]
        price = info["price"]
        item_total = qty * price
        total_price += item_total

        col1, col2, col3, col4, col5 = st.columns([4,1,1,1,1])
        with col1:
            st.write(f"**{name}**")
        with col2:
            st.write(f"Qty: {qty}")
        with col3:
            if st.button(f"➕ Increase - {name}"):
                st.session_state.cart[name]["quantity"] += 1
                st.experimental_rerun()
        with col4:
            if st.button(f"➖ Decrease - {name}"):
                if st.session_state.cart[name]["quantity"] > 1:
                    st.session_state.cart[name]["quantity"] -= 1
                else:
                    del st.session_state.cart[name]
                st.experimental_rerun()
        with col5:
            if st.button(f"❌ Remove - {name}"):
                del st.session_state.cart[name]
                st.experimental_rerun()

    st.markdown("---")
    st.markdown(f"## Total Price: Rs {total_price}")

    if st.button("🧹 Clear Cart"):
        st.session_state.cart = {}
        st.success("Cart cleared.")
else:
    st.write("Your cart is empty.")

# Feedback
st.markdown("---")
st.markdown("### ✍️ Give Your Feedback")
feedback = st.text_area("Your feedback is important to us.", value=st.session_state.feedback, height=100)
if st.button("📤 Send Feedback"):
    if feedback.strip():
        st.session_state.feedback = feedback
        st.success("Thank you! We appreciate your feedback.")
    else:
        st.error("Please write something before sending.")
