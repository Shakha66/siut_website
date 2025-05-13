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
