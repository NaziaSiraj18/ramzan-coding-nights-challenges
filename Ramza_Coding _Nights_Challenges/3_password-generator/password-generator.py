from numpy import character
import streamlit as st     
import random 
import string

def generate_password(Length, use_digits, use_special):
    characters = string.ascii_letters
    
    if use_digits:
        characters += string.digits #Adds numbers (0-9) if selected
    if use_special: 
        characters += string.punctuation #Add special characters (!, @, #, $, ^, &, *)
    
    return ''.join(random.choice(characters) for _ in range(Length))

st.title("Password Generator")
st.write("Generate a strong and secure password")

Length = st.slider("Select the length of the password", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("Include numbers")
use_special = st.checkbox("Include special characters")

if st.button("Generate Password"):
    password = generate_password(Length, use_digits, use_special)
    st.write(f"Generated Password: `{password}`")

st.write("--------------------------")  
st.write("Made with ❤️ by [Nazia Siraj](https://github.com/Naziasiraj18)")  