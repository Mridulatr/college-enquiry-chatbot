
import json
from pathlib import Path

import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA_PATH = Path(__file__).parent / "faq_data.json"

@st.cache_resource
def load_data_and_vectorizer():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    questions = [item["question"] for item in data]
    answers = [item["answer"] for item in data]
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
    X = vectorizer.fit_transform(questions)
    return data, questions, answers, vectorizer, X

data, questions, answers, vectorizer, X = load_data_and_vectorizer()

def get_answer(user_query, topk=3, threshold=0.25):
    query_vec = vectorizer.transform([user_query])
    sims = cosine_similarity(query_vec, X).flatten()
    best_idx = int(sims.argmax())
    best_score = float(sims[best_idx])
    best_answer = answers[best_idx]
    # Top-k suggestions (indices sorted by similarity)
    top_indices = sims.argsort()[::-1][:topk]
    suggestions = [(questions[i], float(sims[i])) for i in top_indices if float(sims[i]) > 0]
    return best_answer, best_score, suggestions

st.set_page_config(page_title="NSSCE Enquiry Chatbot", page_icon="🤖")
st.title("NSSCE College Enquiry Chatbot 🤖")
st.caption("Ask questions about NSS College of Engineering (admissions, courses, contacts, etc.).")

with st.expander("ℹ️ How it works"):
    st.write(
        "This chatbot matches your question with a small FAQ dataset using TF-IDF and cosine similarity. "
        "Expand the dataset in `faq_data.json` to make the bot smarter."
    )

user_query = st.text_input("Type your question here:").strip()

if user_query:
    answer, score, suggestions = get_answer(user_query)
    if score >= 0.25:
        st.success(answer)
    else:
        st.warning("Sorry, I couldn't find an exact answer. Please try rephrasing your question or refer to the official website.")
        if suggestions:
            st.write("Did you mean:")
            for q, s in suggestions:
                st.write(f"- {q}")

st.divider()
with st.expander("📄 View current FAQ dataset"):
    st.json(data, expanded=False)

st.caption("Disclaimer: Always verify critical details on the official website: https://www.nssce.ac.in/")
