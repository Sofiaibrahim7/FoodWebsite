import streamlit as st
import base64

st.set_page_config(page_title="Ice Cream", layout="wide")
st.markdown("## 🍨 Ice Cream Collection (Base64 Embedded Images)")

# Function to convert image file to Base64 string
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# List of ice cream items with local image paths
ice_cream_items = [
    {"img_path": "images/ice1.png", "name": "Strawberry Delight", "price": 150},
    {"img_path": "images/ice2.png", "name": "Chocolate Heaven", "price": 200},
    {"img_path": "images/ice3.png", "name": "Single Scoop Surprise", "price": 180},
]

# Initialize cart
if "cart" not in st.session_state:
    st.session_state.cart = {}

cols = st.columns(len(ice_cream_items))

for i, item in enumerate(ice_cream_items):
    with cols[i]:
        b64_img = get_base64_image(item["img_path"])
        img_html = f'<img src="data:image/png;base64,{b64_img}" width="250">'
        st.markdown(img_html, unsafe_allow_html=True)
        st.markdown(f"**{item['name']}**")
        st.markdown(f"💰 Price: Rs {item['price']}")
        if st.button(f"🛒 Add to Cart - {item['name']}"):
            name = item["name"]
            if name in st.session_state.cart:
                st.session_state.cart[name]["quantity"] += 1
            else:
                st.session_state.cart[name] = {"price": item["price"], "quantity": 1}
            st.success(f"{name} added to cart!")

# Cart display
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
