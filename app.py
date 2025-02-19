import streamlit as st
from sentence_transformers import SentenceTransformer

st.title("Test Sentence Transformers")
st.write("Trying to import SentenceTransformer...")

try:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    st.write("Import successful!")
except Exception as e:
    st.write(f"Error: {e}")
