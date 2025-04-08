import streamlit as st
import streamlit.components.v1 as components

def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,
    }
    
    key = f"{unit_from}_{unit_to}"  
    if key in conversions:
        return value * conversions[key]
    else:
        return "⚠️ Conversion not supported"

# Custom CSS for better styling
st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f4;
        font-family: Arial, sans-serif;
    }
    .stApp {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔄 Unit Converter")

value = st.number_input("✍️ Enter the value:")

unit_from = st.selectbox("🔁 Convert from:", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("🔁 Convert to:", ["meters", "kilometers", "grams", "kilograms"])

if st.button("🚀 Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.success(f"✅ Converted Value: {result}")
