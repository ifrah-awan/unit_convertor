#Project 02: Unit Convertor
#Build a Google Unit Convertor using Python and Streamlit:
import streamlit as st
from pint import UnitRegistry
ureg = UnitRegistry()
#Custom Styling
st.markdown(
    """
    <style>
.stApp {
        background: linear-gradient(to right,rgb(77, 145, 100),rgb(196, 63, 176));
        color: white;
        font-family: Arial, sans-serif;
    }
    .stTextInput, .stSelectbox {
        border-radius: 5px;
        padding: 10px;
    }
    .stButton button {
        background: linear-gradient(to right,rgb(21, 105, 165),rgb(29, 110, 124),rgb(29, 185, 94));
        color: black;
        font-weight: bold;    
</style>
    """,
    unsafe_allow_html=True
)

#page title 
st.markdown("""
<h1 style="text-align:
center;">"  ⚡Smart Unit Converter</h1>
""",
unsafe_allow_html=True)
st.markdown(
    """
    <p style="text-align:
center;font-size:18px;
font-weight:bold;
">⇅ Easily convert units forms
 one to another</p>
 """,
unsafe_allow_html=True)


#Conversion type selection
conversion_type = st.selectbox("Select the Conversion Type", ["length","weight","temperature","volume"])

#define unit option based on type
unit_option={
    "length":["m","km","cm","mm","inch","feet","yard","mile"],
    "weight":["kg","g","mg","lb","oz","ton"],
    "temperature":["celsius","fahrenheit","kelvin"],
    "volume":["litres","ml","gallon","cup"]
 }
#user input for viewers
amount=st.number_input("🔢 Enter value", min_value=0.0,format="%.2f")

#select units
from_unit=st.selectbox("from",unit_option[conversion_type])
to_unit=st.selectbox("To",unit_option[conversion_type])

#convert function
def convert_units(value, from_unit,to_unit):
    if conversion_type =="Temperature":
     if from_unit=="celsius" and to_unit=="Fahrenheit":
           return (value*9/5)+32
     elif from_unit=="celsius" and to_unit=="kelvin":
           return value +273.15
     elif from_unit=="fahrenheit"and to_unit=="celsius":
           return (value-32)*5/9
     elif from_unit=="fahrenhiet"and to_unit=="kelvin":  
           return (value-32)*5/9+273.15
     elif from_unit=="kelvin"and to_unit=="celsius":
           return value-273.15
     elif from_unit=="kelvin"and to_unit=="fahrenhiet":
           return (value-273.15)*9/5+32
     else:
           return value
    else:
           return value * ureg(from_unit).to(to_unit).magnitude

#convert button
if st.button(" 🚀Convert Now!"):
    result = convert_units(amount, from_unit, to_unit)
    st.write(f"**✅Converted Value:** {result:.2f} {to_unit}")

#convert button styling
st.markdown(
    """
    <style>
    .stButton>button{
        background-color:#4CAF50;/*green*/
        color:white;
        font-size:18px;
        padding:10px 20px;
        border-radius:8px;
        border:none;
        transition:background-color 0.3s ease;
        width: 100%;
        margin-top: 10px;
    }
    .stButton>button:hover{
           background-color:#45a049;
           transform:scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
     """
     </style>
     <div class="footer">
     <p>Created by ifrah awan</p>
     </div>
     """,
     unsafe_allow_html=True
)