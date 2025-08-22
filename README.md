
# NSSCE College Enquiry Chatbot 🤖

A lightweight FAQ chatbot for **NSS College of Engineering (NSSCE)** built with **Python**, **TF‑IDF**, and **Streamlit**.

## ✨ Features
- Answers questions related to admissions, affiliation, contacts, etc from a FAQ dataset
- TF‑IDF + cosine similarity for matching
- Shows helpful suggestions when confidence is low
- Easily extendable by editing `faq_data.json`

## 🛠️ Run locally
```bash
# (optional) create a virtual environment first
pip install -r requirements.txt
streamlit run app.py
```

## 📦 Project structure
```
college-enquiry-chatbot/
├─ app.py
├─ faq_data.json
├─ requirements.txt
└─ README.md
```


## ⚠️ Disclaimer
Some answers may change over time. Always verify critical information on the official site: https://www.nssce.ac.in/
