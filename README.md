# 🚗 مترجم عربي - إنجليزي | Arabic-English Translator

تطبيق ويب بسيط لترجمة النصوص من العربي للإنجليزي، باستخدام موديل Seq2Seq
تم تدريبه (fine-tuned) باستخدام مكتبة 🤗 Transformers.

A simple web app that translates Arabic text into English, using a
fine-tuned Seq2Seq model built with 🤗 Transformers and served through Streamlit.

---

## 🔗 Live Demo

[جرب التطبيق من هنا](https://translator-app-mhxo9xhlzhjminzkqvgdre.streamlit.app/)

## 🧠 عن الموديل | About the Model

- **Base model:** [Helsinki-NLP/opus-mt-ar-en](https://huggingface.co/Helsinki-NLP/opus-mt-ar-en)
- **Fine-tuned on:** [opus-100 (ar-en)](https://huggingface.co/datasets/Helsinki-NLP/opus-100)
- **Model hosted on:** Hugging Face Hub → [mwael399/arabic-english-translator](https://huggingface.co/mwael399/arabic-english-translator)

> ملحوظة: الموديل مُدرّب على نصوص فصحى/شبه فصحى، وقد يواجه صعوبة مع اللهجة العامية
> أو المصطلحات التقنية المتخصصة (مثل مصطلحات صيانة السيارات) نظرًا لطبيعة بيانات التدريب.

## ⚙️ التشغيل محليًا | Run Locally

```bash
# 1) Clone the repo
git clone https://github.com/wezoalraye/translator-app.git
cd translator-app

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the app
streamlit run app.py
```

هيفتح التطبيق تلقائيًا على `http://localhost:8501`

## 📦 المكتبات المستخدمة | Tech Stack

- [Streamlit](https://streamlit.io/) – الواجهة
- [🤗 Transformers](https://huggingface.co/docs/transformers) – الموديل والـ tokenizer
- [PyTorch](https://pytorch.org/) – الـ backend للموديل

## 📁 هيكل المشروع | Project Structure

```
translator-app/
├── app.py              # Streamlit app
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## ✍️ المطور | Author

**Mohamed Wael**
NLP Specialist | AI Engineering Student

---

*هذا المشروع جزء من مسار تعليمي شخصي في مجال NLP وRAG systems.*
