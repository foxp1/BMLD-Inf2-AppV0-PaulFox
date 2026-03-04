import streamlit as st
from functions.addition import add

st.title("Rechner")

with st.form("rechner"):
    num1 = st.number_input("num1")
    num2 = st.number_input("num2")

    num3 = st.number_input("num3")

    resultat = add(num1, num2, num3)

    button = st.form_submit_button()

    if button:
        st.write(resultat)