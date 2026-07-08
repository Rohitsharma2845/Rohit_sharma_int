import streamlit as st

st.title("MirAi Internship Landing Page")
st.write("This is a basic UI built with streamlit ")

# TAKE USER INPUT 
user_message = st.text_input("What is your Favourite Country")  # This will create a text box

if st.button("SUBMIT"):
    st.write("Button Pressed")
    st.write("My Favourite Country is ",user_message)

# Task : Create a small Calculator using Streamlit
# learn 5 functions form the documentation that are not discussed in the class


