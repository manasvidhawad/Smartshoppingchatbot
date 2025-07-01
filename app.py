import streamlit as st
import openai
import os

# Load API key from Streamlit secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Smart Shopping Assistant", page_icon="🛒")
st.title("🛒 Smart Shopping Assistant")
st.markdown("Ask me about products, offers, categories, or anything related to your shopping experience!")

user_input = st.text_input("👤 You:", placeholder="e.g. Show me best deals on shoes")

def get_chatbot_response(query):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful in-store shopping assistant. Help customers find products, deals, and give suggestions."},
                {"role": "user", "content": query}
            ]
        )
        return response.choices[0].message.content.strip()

    except openai.error.RateLimitError:
        return "⚠️ You’ve hit the usage limit. Please try again later."
    except openai.error.AuthenticationError:
        return "❌ Invalid API key. Please check your key in Streamlit secrets."
    except Exception as e:
        return f"🚨 An unexpected error occurred: {str(e)}"

if user_input:
    with st.spinner("Thinking..."):
        reply = get_chatbot_response(user_input)
        st.markdown(f"🛍️ **Bot:** {reply}")
