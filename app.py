import streamlit as st

st.title("Echo Chamber 9000")
user_name = st.text_input("Enter your name : ")
user_message = st.text_input("Enter your message : ")

if st.button("Transmit"):
    if user_name == "":
        st.error("Please Enter Your UserName ")
    elif user_message == "":
        st.warning("Please type a message to transmit ")

    else:
        st.success(
            f"Transmmission Successfull ! Greetings {user_name}"
            f"We have received your message: {user_message}"   
                   )
        
        character_count = len(user_message)
        token_count = character_count/4

        st.info(
            f"System Check: Your message will consume approximately "
            f"{token_count:.0f} tokens from our context window."
        )

    