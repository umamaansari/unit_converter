

import streamlit as st

def convert_units(value, unit_from, unit_to):

 conversions = {
    "meters_kilometers" :0.001,
    "kilometers_meters":1000,
    "grams_kilograms":0.001,
    "kilograms_grams":1000
}
 key = f"{unit_from}_{unit_to}"

 if key in conversions:
  conversion = conversions[key]
  return value * conversion
 else:
  return "conversion not supported"
 
st.title( """Unit Converter 📝
          Made by Umama Ansari 💖""")

value = st.number_input("Enter the value:",)

unit_from = st.selectbox("convert from:", ["meters","kilometers","grams", "kilograms"])

unit_to = st.selectbox("convert to :", ["meters", "kilometers","grams", "kilograms"])

if st.button("convert"):
  
  result = convert_units(value,unit_from, unit_to)
  st.write(f"converted value: {result}")

 