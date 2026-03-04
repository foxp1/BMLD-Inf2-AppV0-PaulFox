import streamlit as st
from functions.temperatur import celsius_to_fahrenheit

st.title("Temperatur Rechner")

st.write("Mein Rechner für die Umrechnung von Celsius zu Fahrenheit")

with st.form("my_form"):
    celsius = st.number_input("Gib die Temperatur in Celsius ein:")
    submit_button = st.form_submit_button("Umrechnen")
    if submit_button:
        fahrenheit = celsius_to_fahrenheit(celsius)
        st.write(f"Die Temperatur in Fahrenheit ist: {fahrenheit}")
st.write("Outside the form")