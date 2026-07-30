import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# غيّر ده لاسم الموديل بتاعك على HF
MODEL_NAME = "mwael399/arabic-english-translator"

st.set_page_config(
    page_title="مترجم عربي - إنجليزي",
    page_icon="🚗",
    layout="centered",
)

# ---------- CSS للتنسيق واتجاه RTL ----------
st.markdown("""
<style>
    .main {
        direction: rtl;
    }
    .stTextArea textarea {
        direction: rtl;
        text-align: right;
        font-size: 17px;
        border-radius: 10px;
    }
    .title-container {
        text-align: center;
        padding: 10px 0 5px 0;
    }
    .title-container h1 {
        font-size: 2.2rem;
        margin-bottom: 0;
    }
    .subtitle {
        text-align: center;
        color: #9CA3AF;
        font-size: 1rem;
        margin-bottom: 25px;
    }
    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        padding: 10px 0;
        font-weight: 600;
        background-color: #DC2626;
        color: white;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #B91C1C;
        color: white;
    }
    .result-box {
        background-color: #14532D;
        border-radius: 10px;
        padding: 18px;
        margin-top: 15px;
        font-size: 1.1rem;
        color: #ffffff;
        direction: ltr;
        text-align: left;
    }
    .result-label {
        direction: rtl;
        text-align: right;
        color: #86EFAC;
        font-size: 0.9rem;
        margin-bottom: 6px;
    }
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------- تحميل الموديل ----------
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    return tokenizer, model

with st.spinner("جاري تحميل الموديل..."):
    tokenizer, model = load_model()

# ---------- الواجهة ----------
st.markdown("""
<div class="title-container">
    <h1>🚗 مترجم عربي - إنجليزي</h1>
</div>
<div class="subtitle">مترجم مخصص لمصطلحات صيانة السيارات</div>
""", unsafe_allow_html=True)

text = st.text_area("النص بالعربي:", height=120, placeholder="اكتب جملتك هنا...")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    translate_clicked = st.button("ترجم 🔄")

if translate_clicked:
    if text.strip() == "":
        st.warning("من فضلك اكتب نص أولاً")
    else:
        with st.spinner("جاري الترجمة..."):
            inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
            outputs = model.generate(**inputs, max_length=128)
            translation = tokenizer.decode(outputs[0], skip_special_tokens=True)

        st.markdown(f"""
        <div class="result-label">الترجمة:</div>
        <div class="result-box">{translation}</div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.caption("Powered by Hugging Face Transformers • Fine-tuned Seq2Seq model")
