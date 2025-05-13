import streamlit as st

# Language selector
language = st.sidebar.selectbox("Choose Language / Tilni tanlang / Выберите язык", ["English", "Uzbek", "Russian"])
# Dictionary for multilingual content
content = {
    "English": {
        "title": "Samarkand International University of Technology (SIUT)",
        "admissions": "Admissions are open for the upcoming academic year. Apply online through our website. Requirements include academic transcripts, a valid ID/passport, and proof of English proficiency.",
        "tuition": "Tuition fees vary depending on the program. On average, annual tuition ranges from $2,500 to $4,000. Scholarships may be available.",
        "dormitories": "SIUT provides modern dormitory facilities for both local and international students, with options for shared or private rooms.",
        "scholarships": "SIUT offers merit-based and need-based scholarships. Early applicants may also be eligible for special financial aid.",
        "programs": "Our programs include Computer Science, Artificial Intelligence, Engineering, and Business Technology. All programs are aligned with international standards.",
        "application": "Applications are submitted online. Visit our official website, complete the form, and upload required documents. Application deadlines vary by semester.",
        "contact": "Email: info@siut.uz | Phone: +998 71 200 00 00 | Address: University Campus, Samarkand, Uzbekistan",
        "language": "All programs are taught in English. Some support is available in Uzbek and Russian.",
        "student_life": "SIUT hosts various student clubs, cultural events, and hackathons. Our campus is vibrant, inclusive, and tech-driven."
    },
    "Uzbek": {
        "title": "Samarqand Xalqaro Texnologiya Universiteti (SIUT)",
        "admissions": "Yangi o'quv yili uchun qabul ochiq. Arizalarni rasmiy veb-sayt orqali topshiring. Talablar: diplom nusxalari, ID yoki pasport va ingliz tilini bilish darajasi.",
        "tuition": "O'qish narxi tanlangan dasturga qarab farq qiladi. Yillik o'rtacha to'lov $2,500 dan $4,000 gacha. Ba'zi holatlarda grantlar mavjud.",
        "dormitories": "SIUT talabalar uchun zamonaviy yotoqxona sharoitlarini taqdim etadi. Yotoqxonalar umumiy yoki yakka xonalardan iborat.",
        "scholarships": "Universitet iqtidorli va ehtiyojmand talabalar uchun grantlar taqdim etadi. Erta ro'yxatdan o'tganlar alohida imtiyozga ega bo'lishi mumkin.",
        "programs": "Bizda Kompyuter fanlari, Sun’iy intellekt, Muhandislik va Biznes texnologiyalari bo‘yicha dasturlar mavjud.",
        "application": "Arizalarni onlayn tarzda yuboring. Rasmiy saytga kirib, shaklni to‘ldiring va zarur hujjatlarni yuklang.",
        "contact": "Email: info@siut.uz | Tel: +998 71 200 00 00 | Manzil: Universitet shaharchasi, Samarqand, O‘zbekiston",
        "language": "Barcha darslar ingliz tilida o‘qitiladi. Qo‘shimcha tarzda o‘zbek va rus tillarida yordam beriladi.",
        "student_life": "SIUTda turli klublar, madaniy tadbirlar va xakatonlar tashkil etiladi. Universitet hayoti faol va texnologiyaga boy."
    },
    "Russian": {
        "title": "Самаркандский Международный Технологический Университет (SIUT)",
        "admissions": "Прием открыт на следующий учебный год. Подайте заявку через наш официальный сайт. Требования: аттестат, паспорт и знание английского языка.",
        "tuition": "Стоимость обучения зависит от программы и составляет в среднем от $2,500 до $4,000 в год. Возможны стипендии.",
        "dormitories": "SIUT предоставляет современные общежития для местных и иностранных студентов. Доступны как общие, так и отдельные комнаты.",
        "scholarships": "Университет предлагает стипендии на основе успеваемости и финансовых потребностей. Ранние заявки могут получить дополнительные льготы.",
        "programs": "Программы включают компьютерные науки, искусственный интеллект, инженерное дело и бизнес-технологии.",
        "application": "Подача заявок осуществляется онлайн. Посетите наш сайт, заполните форму и загрузите необходимые документы.",
        "contact": "Email: info@siut.uz | Телефон: +998 71 200 00 00 | Адрес: Университетский городок, Самарканд, Узбекистан",
        "language": "Все программы преподаются на английском языке. Также доступна поддержка на узбекском и русском.",
        "student_life": "Университет предлагает студенческие клубы, культурные мероприятия и хакатоны. Кампус активный и ориентирован на технологии."
    }
}

# Load selected language content
st.title(content[language]["title"])

st.header("🎓 Admissions")
st.write(content[language]["admissions"])

st.header("💸 Tuition")
st.write(content[language]["tuition"])

st.header("🏠 Dormitories")
st.write(content[language]["dormitories"])

st.header("🎓 Scholarships")
st.write(content[language]["scholarships"])

st.header("📚 Programs")
st.write(content[language]["programs"])

st.header("📝 Application Method")
st.write(content[language]["application"])

st.header("🌍 Language of Instruction")
st.write(content[language]["language"])

st.header("🏫 Student Life")
st.write(content[language]["student_life"])

st.header("📩 Contact Info")
st.write(content[language]["contact"])


import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from langdetect import detect
import numpy as np

# FAQ Data
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

# Chatbot response function
def get_chatbot_response(user_input):
    try:
        lang = detect(user_input)
    except:
        return "Sorry, I couldn't detect the language. Please try again."

    if lang not in faq_data:
        return "Sorry, I can only respond in English, Russian, or Uzbek."

    questions = list(faq_data[lang].keys())
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(questions)
    user_vec = vectorizer.transform([user_input.lower()])
    similarity = cosine_similarity(user_vec, tfidf)
    best_match_idx = np.argmax(similarity)
    confidence = similarity[0][best_match_idx]

    if confidence < 0.3:
        return "I'm not sure how to answer that. Please ask a different question."

    best_question = questions[best_match_idx]
    return faq_data[lang][best_question]

# Streamlit UI
st.set_page_config(page_title="SIUT Chatbot")
st.title("🤖 SIUT Multilingual Chatbot")
st.write("Ask me about admissions, programs, dorms, tuition, etc. (English, Uzbek, Russian supported)")

user_query = st.text_input("Your question")

if user_query:
    response = get_chatbot_response(user_query)
    st.markdown(f"**Bot:** {response}")
