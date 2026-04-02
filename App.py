import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Pronostic VIP", layout="wide")

# Style Blanc et Rouge
st.markdown("""
    <style>
    .main { background-color: #FFFFFF; }
    h1, h2, h3 { color: #FF0000 !important; }
    .stButton>button { background-color: #FF0000; color: white; border-radius: 8px; width: 100%; }
    </style>
    """, unsafe_allow_index=True)

# Choix de la langue
lang = st.sidebar.selectbox("Language / Langue", ["Français", "English"])

if lang == "Français":
    st.title("🏆 Pronostic VIP")
    st.subheader("À propos de nous")
    st.write("Bienvenue ! Nous utilisons des modèles mathématiques pour vos analyses sportives.")
    menu = ["Accueil", "Pronos Free", "Accès VIP", "Live Score"]
else:
    st.title("🏆 Pronostic VIP")
    st.subheader("About Us")
    st.write("Welcome! We use mathematical models for your sports analysis.")
    menu = ["Home", "Free Pronos", "VIP Access", "Live Score"]

choice = st.sidebar.radio("Menu", menu)

# Contenu des pages
if choice in ["Accueil", "Home"]:
    st.write("---")
    st.info("Sélectionnez une option dans le menu à gauche / Select an option from the menu on the left.")

elif choice in ["Pronos Free", "Free Pronos"]:
    st.header("⚽ Free Predictions")
    st.write("1. Match A - Over 2.5")
    st.write("2. Match B - Win Home")
    # هنا غنزيدو من بعد الـ 10 توقعات كاملين

elif choice in ["Accès VIP", "VIP Access"]:
    st.header("💎 VIP Area")
    password = st.text_input("Password / Mot de passe", type="password")
    if password == "1234": # كود مؤقت
        st.success("Correct!")
        st.write("🔥 VIP Match 1: X vs Y - Tip: Draw")
    elif password != "":
        st.error("Incorrect!")

elif choice == "Live Score":
    st.header("⏱️ Live Score")
    st.write("Interface Live Score à venir...")
