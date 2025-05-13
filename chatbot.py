import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# FAQ data
faq_data = {
    "en": {
        "what is siut": "SIUT stands for Samarkand International University of Technology, a modern higher education institution in Uzbekistan.",
        "where is siut located": "SIUT is located in Samarkand, Uzbekistan.",
        "how do i apply to siut": "You can apply to SIUT through the official website by filling out the online application form.",
        "what are the admission requirements": "Admission requirements vary by program but generally include transcripts, English proficiency, and an entrance exam.",
        "what is the tuition fee": "Tuition fees depend on the program. Check the official SIUT website for current information.",
        "does siut provide dormitories": "Yes, SIUT offers student dormitories for both local and international students.",
        "does siut offer scholarships": "Yes, SIUT provides merit-based and need-based scholarships.",
        "what programs does siut offer": "SIUT offers programs in technology, engineering, computer science, and business.",
        "what language are courses taught in": "Most courses at SIUT are taught in English.",
        "how can i contact siut": "You can contact SIUT through the website or by emailing info@siut.uz."
    },
    "uz": {
        "siut nima": "SIUT — bu Samarqand Xalqaro Texnologiya Universiteti, zamonaviy oliy o‘quv yurti.",
        "siut qayerda joylashgan": "SIUT Samarqand shahrida joylashgan.",
        "siutga qanday ariza topshiraman": "Siz SIUTga rasmiy veb-sayti orqali ariza topshirishingiz mumkin.",
        "qabul qilish talablari qanday": "Qabul talablari dasturga qarab o‘zgaradi, lekin odatda diplom, ingliz tili darajasi va test talab qilinadi.",
        "kontrakt summasi qancha": "To‘lov miqdori dasturga qarab farq qiladi. Rasmiy saytdan tekshiring.",
        "yotoqxona mavjudmi": "Ha, SIUT talabalar uchun yotoqxonalar taqdim etadi.",
        "stipendiyalar bormi": "Ha, SIUT turli stipendiyalarni taklif qiladi.",
        "qanday dasturlar mavjud": "SIUTda texnologiya, muhandislik, IT va biznes sohalari bo‘yicha dasturlar mavjud.",
        "darslar qaysi tilda o‘tiladi": "Asosan barcha darslar ingliz tilida olib boriladi.",
        "siut bilan qanday bog‘lansam bo‘ladi": "Siz SIUTga rasmiy sayti yoki info@siut.uz elektron pochtasi orqali bog‘lanishingiz mumkin."
    },
    "ru": {
        "что такое siut": "SIUT — это Самаркандский Международный Технологический Университет, современное учебное заведение в Узбекистане.",
        "где находится siut": "SIUT находится в Самарканде, Узбекистан.",
        "как подать заявку в siut": "Вы можете подать заявку через официальный сайт SIUT, заполнив онлайн-форму.",
        "каковы требования к поступающим": "Требования зависят от программы, обычно нужны документы, знание английского и вступительный экзамен.",
        "сколько стоит обучение": "Стоимость зависит от программы. Актуальная информация указана на сайте.",
        "есть ли общежитие": "Да, SIUT предоставляет общежития для студентов.",
        "предоставляются ли стипендии": "Да, университет предлагает академические и социальные стипендии.",
        "какие программы доступны": "В SIUT есть программы по технологиям, инженерии, IT и бизнесу.",
        "на каком языке проходят занятия": "Основной язык обучения — английский.",
        "как связаться с siut": "Вы можете написать на почту info@siut.uz или использовать форму на сайте."
    }
}

# Response logic
def get_multilingual_response(user_input, data):
    user_input = user_input.lower()
    best_match = ""
    best_lang = ""
    highest_score = 0.0

    for lang, qa_pairs in data.items():
        questions = list(qa_pairs.keys())
        vectorizer = TfidfVectorizer().fit(questions + [user_input])
        tfidf = vectorizer.transform(questions + [user_input])
        similarity = cosine_similarity(tfidf[-1], tfidf[:-1])
        max_score = np.max(similarity)
        if max_score > highest_score:
            highest_score = max_score
            best_lang = lang
            best_match = questions[np.argmax(similarity)]

    if highest_score < 0.3:
        return "Sorry, I didn't understand that. Could you rephrase?"
    return data[best_lang][best_match]

# Streamlit UI
st.set_page_config(page_title="SIUT Website", layout="wide")
st.title("🎓 Samarkand International University of Technology")

st.sidebar.header("Navigation")
section = st.sidebar.radio("Go to:", ["Home", "Admissions", "Programs", "Chatbot"])

if section == "Home":
    st.header("Welcome to SIUT")
    st.write("SIUT is a modern technological university located in Samarkand, Uzbekistan. Explore our programs and offerings.")
elif section == "Admissions":
    st.header("Admissions")
    st.write("Find out how to apply, requirements, tuition, and scholarships.")
elif section == "Programs":
    st.header("Academic Programs")
    st.write("We offer cutting-edge programs in Technology, Engineering, Computer Science, and Business.")
elif section == "Chatbot":
    st.header("🤖 SIUT FAQ Chatbot")
    st.write("Ask your question below in English, Uzbek, or Russian:")
    user_input = st.text_input("Your question:")
    if user_input:
        response = get_multilingual_response(user_input, faq_data)
        st.success(response)
