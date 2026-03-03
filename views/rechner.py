import streamlit as st
from functions.test import add

st.title("A + B = C")

with st.form("add_form"):
    st.write("Enter the numbers to add")


    number1 = st.text_input("Number 1", "Enter your number here...")


    number2 = st.slider("Form slider")
    

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write("Sum: ", add(number1, number2))

st.write("Diese Seite ist eine Unterseite der Startseite.")
