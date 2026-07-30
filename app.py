import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline(
        "translation_ar_to_en",
        model="mwael399/arabic-english-translator"
    )

translator = load_model()

st.title("Arabic → English Translator")

text = st.text_area("Enter Arabic text")

if st.button("Translate"):
    result = translator(text)
    st.success(result[0]["translation_text"])
