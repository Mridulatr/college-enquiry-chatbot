
# NSSCE College Enquiry Chatbot 🤖

A lightweight FAQ chatbot for **NSS College of Engineering (NSSCE)** built with **Python**, **TF‑IDF**, and **Streamlit**.

## ✨ Features
- Answers common questions (admissions, affiliation, contacts, etc.) from a small FAQ dataset
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

## 🚀 Deploy (Streamlit Community Cloud)
1. Push this folder to a new GitHub repository (e.g., `college-enquiry-chatbot`).
2. Go to https://streamlit.io/cloud and sign in.
3. Click **New app** → select your repo → `main` branch → `app.py` as entrypoint.
4. Click **Deploy**. Your app URL will be generated (add the link to your resume!).

## 🧠 Improve the bot
- Add more Q&A pairs in `faq_data.json`. Include synonyms or alternate phrasings as separate entries.
- Tune the threshold in `app.py` (`threshold=0.25`) if matching feels too strict/lenient.
- Add categories (Admissions, Courses, Placements) and filter by category before matching.
- Switch to semantic search (e.g., Sentence Transformers) if you want smarter matching later.

## ⚠️ Disclaimer
Some answers may change over time. Always verify critical information on the official site: https://www.nssce.ac.in/
