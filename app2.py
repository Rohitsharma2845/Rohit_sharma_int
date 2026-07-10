import streamlit as st
st.title("THE MULTIVERSE OF CHATBOTS")

st.write(
    "Choose a chatbot persona, enter your name and message, then click Send."
)

personality = st.selectbox("who do u want to talk to?",[
    "Virat Kholi" , "Rohit Sharma", "Mahendra Singh Dhoni "
]
)

from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key=os.getenv("OPEN_API_KEY"))

user_name = st.text_input("Enter Your Name")
user_message = st.text_input("Say_something : ")

# CLASS WORK

# if st.button("SEND"):
#     if user_message:
#         ai_instructions= f"You are acting as {personality}.Respond to the message sent by the user staying completely in character: {user_message} "
        
#         with st.spinner("Connecting to the Multiverse!........"):
#             response = client.models.generate_content(
#                 model = "gemini-2.5-flash",
#                 contents = ai_instructions
#             )
                
#             st.success("Message received!")
#             st.write(response.text)

#     else:
#         st.warning("Please type a message first ")

# SELF HOMEWORK


if st.button("SEND"):

    if user_name == "":
        st.error("Please provide your name.")

    elif user_message == "":
        st.warning("Please type a message first.")

    else:
        st.success(
            f"Transmission successful! Greetings, {user_name}. "
            f"We received your message: {user_message}"
        )

        char_count = len(user_message)

        token_count = round(char_count / 4)

        st.info(
            f"System Check: Your message will consume approximately "
            f"{token_count} tokens from our context window."
        )

        ai_instructions = f"""
        You are acting as {personality}.

        Respond exactly like {personality}.

        User name: {user_name}

        User message:
        {user_message}
        """

        with st.spinner("Connecting to the Multiverse!........."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=ai_instructions
            )

        st.subheader(f"{personality} says:")

        st.write(response.text)



