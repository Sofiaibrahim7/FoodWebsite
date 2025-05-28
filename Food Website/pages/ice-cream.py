import streamlit as st

# Page setup
st.set_page_config(page_title="Ice Cream", layout="wide")
st.markdown("## 🍨 Ice Cream Collection")

# Initialize cart if not present
if "cart" not in st.session_state:
    st.session_state.cart = {}

# Ice cream items
ice_cream_items = [
    {"img": "images/ice1.png", "name": "Strawberry Delight", "price": 150},
    {"img": "images/ice2.png", "name": "Chocolate Heaven", "price": 200},
    {"img": "images/ice3.png", "name": "Single Scoop Surprise", "price": 180},
]

# Display each item in a column
cols = st.columns(3)
for i, item in enumerate(ice_cream_items):
    with cols[i]:
        st.image(item["img"], width=250)
        st.markdown(f"**{item['name']}**")
        st.markdown(f"💰 Price: Rs {item['price']}")
        if st.button(f"🛒 Add to Cart - {item['name']}"):
            name = item["name"]
            if name in st.session_state.cart:
                st.session_state.cart[name]["quantity"] += 1
            else:
                st.session_state.cart[name] = {"price": item["price"], "quantity": 1}
            st.success(f"{name} added to cart!")

# Cart Section
st.markdown("### 🛒 Your Cart")

if st.session_state.cart:
    total_price = 0
    for name, info in list(st.session_state.cart.items()):
        qty = info["quantity"]
        price = info["price"]
        item_total = qty * price
        total_price += item_total
        col1, col2, col3, col4 = st.columns([4, 1, 2, 1])
        with col1:
            st.write(f"**{name}**")
        with col2:
            st.write(f"Qty: {qty}")
        with col3:
            st.write(f"Rs {item_total}")
        with col4:
            if st.button(f"❌ Remove - {name}"):
                del st.session_state.cart[name]
                st.experimental_rerun()

    st.markdown("---")
    st.markdown(f"## 💵 Total Price: Rs {total_price}")
    
    if st.button("🧹 Clear Cart"):
        st.session_state.cart = {}
        st.success("Cart has been cleared.")
else:
    st.info("🛒 Your cart is empty.")

# Feedback Section
st.markdown("### ✍️ Give Your Feedback")
feedback = st.text_area("Your feedback is important to us.", height=100)
if st.button("📤 Send Feedback"):
    if feedback.strip():
        st.success("Thank you! We appreciate your feedback.")
        st.session_state.feedback = feedback
    else:
        st.error("Please write something before sending.")
