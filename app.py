import os
import streamlit as st
from openai import OpenAI

# Replace with your OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
  # Better: use environment variable

st.set_page_config(page_title="Smart Shopping Assistant")
st.title("🛒 Smart Shopping Assistant")
st.markdown("Ask me about products, categories, deals, or anything you need help with!")

# Input from user
user_input = st.text_input("👤 You:")

# Function to get response from OpenAI
def get_chatbot_response(user_query):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if available
        messages=[
            {"role": "system", "content": "You are a helpful shopping assistant that helps customers find products in a store."},
            {"role": "user", "content": user_query}
        ]
    )
    return response.choices[0].message.content

# Display response
if user_input:
    response = get_chatbot_response(user_input)
    st.markdown(f"🛍️ Bot: {response}")
