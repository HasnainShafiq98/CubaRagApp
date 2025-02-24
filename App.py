import streamlit as st
from RagApp import get_rag_response  # Import chatbot function

st.set_page_config(page_title="Cuba Travel Chatbot", layout="wide")


st.title("🇨🇺 Cuba Travel Chatbot")
st.write("Ask me anything about Cuba, including places to visit, travel tips, and hotels.")

query = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if query:
        with st.spinner("🔍 Searching..."):
            response = get_rag_response(query)
        st.write("### Response:")
        st.write(response)
    else:
        st.warning("⚠️ Please enter a question.")