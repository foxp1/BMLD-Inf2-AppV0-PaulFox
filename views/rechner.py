import streamlit as st
from functions.addition import add, subtract

st.title("Addition Rechner")

st.write("Mein Rechner für die Addition von zwei Zahlen")

with st.form("addition_form"):
    a = st.number_input("Zahl A", value=0)
    b = st.number_input("Zahl B", value=0)
    submit = st.form_submit_button("Berechnen")

st.write(add(a, b))