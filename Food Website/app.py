import streamlit as st
import datetime

st.set_page_config(page_title="FastFood", layout="wide")

# --- Menu Items ---
MENU = [
    {"id": 1, "name": "Pizza", "price": 799, "image": "images/pizza.png", "description": "Classic cheese and tomato pizza."},
    {"id": 2, "name": "Zinger Burger", "price": 499, "image": "images/zinger.png", "description": "Crispy chicken zinger with fries."},
    {"id": 3, "name": "Spaghetti", "price": 699, "image": "images/spaghetti.png", "description": "Italian pasta with meat sauce."},
    {"id": 4, "name": " Beef Biryani", "price": 549, "image": "images/biryani.png", "description": "Aromatic rice with spiced chicken."},
    {"id": 5, "name": " Sandwich", "price": 299, "image": "images/sandwich.png", "description": "Veggies, cheese, and grilled bread."},
    {"id": 6, "name": "Chiken Karahi", "price": 899, "image": "images/karahi.png", "description": "Spicy Pakistani-style mutton curry."}
]

if "cart" not in st.session_state:
    st.session_state.cart = []

if "order_placed" not in st.session_state:
    st.session_state.order_placed = False

# --- Helper Functions ---
def add_to_cart(item):
    for cart_item in st.session_state.cart:
        if cart_item["id"] == item["id"]:
            cart_item["quantity"] += 1
            return
    st.session_state.cart.append({**item, "quantity": 1})

def remove_from_cart(item_id):
    st.session_state.cart = [item for item in st.session_state.cart if item["id"] != item_id]

def increase_quantity(item_id):
    for item in st.session_state.cart:
        if item["id"] == item_id:
            item["quantity"] += 1
            break

def decrease_quantity(item_id):
    for item in st.session_state.cart:
        if item["id"] == item_id:
            item["quantity"] -= 1
            if item["quantity"] <= 0:
                st.session_state.cart.remove(item)
            break

def calculate_total():
    return sum(item["price"] * item["quantity"] for item in st.session_state.cart)

def currency_format(amount):
    return f"Rs {amount:,}"

# --- UI Sections ---
st.markdown("""
    <div style='background-color:#d90429;padding:30px;border-radius:10px;text-align:center;'>
        <h1 style='color:#ffffff;margin:0;font-size:42px;'>🔥 FastFood App</h1>
        <p style='color:#ffffff;font-size:18px;'>Order your favorite meals with a single click!</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("### 📋 Our Menu")
cols = st.columns(3)
for idx, item in enumerate(MENU):
    with cols[idx % 3]:
        if item.get("image"):
            st.image(item["image"], width=300)
        st.markdown(f"**{item['name']}**")
        st.caption(item["description"])
        st.markdown(f"💵 {currency_format(item['price'])}")
        st.button("➕ Add to Cart", key=f"add_{item['id']}", on_click=add_to_cart, args=(item,))

# --- Cart ---
st.markdown("---")
st.markdown("## 🛒 Your Cart")
if not st.session_state.cart:
    st.info("🧺 Your cart is empty.")
else:
    for item in st.session_state.cart:
        col1, col2, col3, col4 = st.columns([4, 1, 1, 1])
        with col1:
            st.markdown(f"**{item['name']}** (Rs {item['price']})")
        with col2:
            st.button("➖", key=f"dec_{item['id']}", on_click=decrease_quantity, args=(item["id"],))
        with col3:
            st.markdown(f"**{item['quantity']}**")
        with col4:
            st.button("➕", key=f"inc_{item['id']}", on_click=increase_quantity, args=(item["id"],))

    total = calculate_total()
    st.markdown(f"### 🧾 Total: {currency_format(total)}")

    name = st.text_input("👤 Name")
    contact = st.text_input("📱 Contact Number")

    if st.button("✅ Place Order"):
        if name and contact:
            st.session_state.order_placed = True
            st.session_state.name = name
            st.session_state.contact = contact
            st.session_state.total = total
            st.success(f"🎉 Order placed successfully! Thank you, {name}. Total: {currency_format(total)}")
        else:
            st.error("⚠️ Please enter both name and contact number.")

# --- Receipt ---
if st.session_state.order_placed:
    st.markdown("---")
    st.markdown("## 📄 Order Receipt")
    st.markdown(f"**👤 Name:** {st.session_state.name}")
    st.markdown(f"**📞 Contact:** {st.session_state.contact}")
    st.markdown(f"**📅 Date & Time:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    st.markdown("### 🧾 Items Ordered:")
    for item in st.session_state.cart:
        st.markdown(f"- {item['name']} x {item['quantity']} = {currency_format(item['price'] * item['quantity'])}")
    st.markdown(f"### 🔻 Grand Total: {currency_format(st.session_state.total)}")
    st.success("✅ Please keep this receipt. Your order is being prepared!")
    st.session_state.cart = []
    st.session_state.order_placed = False
