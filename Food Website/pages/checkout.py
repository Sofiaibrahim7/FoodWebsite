import streamlit as st

st.set_page_config(page_title="Checkout", layout="wide")
st.title("🧾 Checkout Page")

if "cart" not in st.session_state or not st.session_state.cart:
    st.warning("🛒 Your cart is empty. Add items first!")
else:
    total = 0
    st.markdown("### 📦 Items in Your Order")

    # ✅ Correct loop
    for name, item in st.session_state.cart.items():
        item_total = item['price'] * item['quantity']
        st.write(f"**{name}** — Rs {item['price']} x {item['quantity']} = Rs {item_total}")
        total += item_total

    st.markdown(f"## 🧮 Total Amount: Rs {total}")

    # 📝 User details
    st.markdown("### 🧍 Customer Information")
    name = st.text_input("Name")
    address = st.text_area("Address")
    phone = st.text_input("Phone Number")

    # ✅ Place Order Button
    if st.button("✅ Place Order"):
        if name and address and phone:
            st.success("🎉 Order placed successfully!")
            st.session_state.cart.clear()  # Clear cart after order
        else:
            st.error("Please fill in all the required information.")
