import streamlit as st

st.title("BASIC CALCULATOR")

# input numbers

input1 = st.number_input("enter 1st number : ")
input2 = st.number_input("enter 2nd number : ")

# Operation Selection 

operation = st.selectbox(
    "Choose Operation",
    [
        "Addition",
        "Substraction",
        "Multiplication",
        "Division",
    ]
)

# Calculate button


if st.button("Calculate"):
    if operation == "Addition":
        result = input1 + input2
    elif operation == "Substraction":
        result = input1-input2
    elif operation == "Multiplication":
        result = input1*input2
    elif operation == "Division":
        if(input2 == 0):
            st.error("Cannot Divide By Zero")
            st.stop()
        result = input1/input2

    st.success(f"result : {result}")
   