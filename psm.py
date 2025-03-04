import re
import streamlit as st

# page styling


st.set_page_config(page_title="Password Strength Checker by Arsalan", page_icon="🔒", layout="centered")
# CSS styling
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton {width: 50%; background-color: #f63366; color: white; font-size: 18px:}
    .stButton:hover {background-color: #f63366; color: white;}
</style>
""", unsafe_allow_html=True)

# Page Title
st.title("🔒Password Strength Generator")
st.write("Enter your password to check its strength.🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9) **.")

        # Special characters
    if re.search(r"[ !@#$%^&*()_+{}\[\]:;\"'<,>.?/\\|`~]", password):
        score += 1 
    else:
        feedback.append("❌ Include **at least one special character ( !@#$%^&*()_+{}\[\]:;\"'<,>.?/\\|`~)**.")

        # Display Password Strength Result
    if score == 4:
        st.success("✅ Your password is **Strong**.")
    elif score >= 3 :
        st.info("⚠️ ** Moderate Password** - Consider improving security by adding more feature.")
    else:
        st.error("❌ **Weak Password** - Please follow the below suggestions to make it strong.")

        # Display feedback
        if feedback:
            with st.expander(" 🔍 **Improvement Suggestions** "):
                for item in feedback:
                    st.write(item)
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong.🔐")

# Button to check password strength
if st.button("Check Strength"):
    if password:
        check_password_strength(password)

    else:
        st.warning("⚠️ Please enter your password to check its strength.")