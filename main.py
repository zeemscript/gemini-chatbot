import streamlit as st
import google.generativeai as genai

# Configure the Google Gemini API
genai.configure(api_key="AIzaSyCAOvmdRTfN9BCAWcACukXRItenG9t5sBA")

# Set up the Streamlit page
st.header("Zeemscript GEMINI Chatbot")


user_input = st.chat_input("Enter your message...")

# Check if there is a user input
if user_input:
    # Append user message to the chat history immediately
    st.session_state["chat_history"].append({"role": "user", "content": user_input})

    # Display the user's message immediately
    st.chat_message("user").write(user_input)

    # Send user input to Gemini model and get response
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(user_input)

    # Extract the response content
    bot_response = ""
    if response.candidates:
        content = response.candidates[0].content  # Access the 'content' attribute
        bot_response = content.parts[0].text  # Access the first part's text

    # Append bot response to the chat history
    st.session_state["chat_history"].append({"role": "assistant", "content": bot_response})

    # Display the assistant's response
    st.chat_message("assistant").write(bot_response)

# Display the chat history in the correct order
if st.session_state["chat_history"]:
    for message in st.session_state["chat_history"]:
        role = message["role"]
        content = message["content"]
        st.chat_message(role).write(content)
