
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "mwael399/arabic-english-translator"

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    return tokenizer, model

tokenizer, model = load_model()

st.title("مترجم عربي - إنجليزي 🚗")
st.write("اكتب جملة بالعربي وهتترجملك على طول")

text = st.text_area("النص بالعربي:", height=100)

if st.button("ترجم"):
    if text.strip() == "":
        st.warning("اكتب نص الأول")
    else:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
        outputs = model.generate(**inputs, max_length=128)
        translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
        st.success("الترجمة:")
        st.write(translation)
