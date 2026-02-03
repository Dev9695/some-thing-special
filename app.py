import streamlit as st
import random
import time
import os
from datetime import date

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(page_title="Dev ❤️ Kittu", page_icon="💘", layout="centered")

GF_NAME = "Kittu"
YOUR_NAME = "Dev"
SECRET_PASSWORD = "kittu1508"

FIRST_MEET_DATE = date(2023, 8, 15)
RELATIONSHIP_DATE = date(2023, 9, 1)

# -----------------------------
# CSS THEME + HEARTS ANIMATION
# -----------------------------
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(180deg, #ffe6f0 0%, #fff0f5 60%, #ffffff 100%);
}
html, body, [class*="css"]  {
    color: black !important;
}

/* Titles */
h1, h2, h3 {
    font-family: 'Segoe UI', sans-serif;
}

/* Center & Rounded containers */
.block-container {
    padding-top: 2rem;
}

/* Buttons style */
.stButton button {
    border-radius: 18px;
    border: 0px;
    padding: 10px 22px;
    font-size: 18px;
    font-weight: 700;
    transition: 0.2s ease-in-out;
}
.stButton button:hover {
    transform: scale(1.06);
}

/* Cute Card */
.val_card {
    background: rgba(255,255,255,0.65);
    border-radius: 20px;
    padding: 18px;
    box-shadow: 0px 8px 20px rgba(255, 0, 100, 0.15);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.45);
}
.fall {
  position: fixed;
  top: -20px;
  animation: fallDown 8s linear infinite;
  font-size: 22px;
  opacity: 0.75;
}
@keyframes fallDown {
  0% {transform: translateY(0) translateX(0); opacity: 0.9;}
  100% {transform: translateY(110vh) translateX(30px); opacity: 0.0;}
}


/* Floating hearts */
.heart {
  position: fixed;
  bottom: -20px;
  animation: floatUp 8s linear infinite;
  font-size: 22px;
  opacity: 0.7;
}
@keyframes floatUp {
  0% {transform: translateY(0) translateX(0); opacity: 0.9;}
  100% {transform: translateY(-110vh) translateX(40px); opacity: 0.0;}
}
</style>
<div class="heart" ...>💖</div>
<div class="fall" style="left: 10%; animation-delay: 0s;">💗</div>
<div class="fall" style="left: 25%; animation-delay: 1s;">💖</div>
<div class="fall" style="left: 40%; animation-delay: 2s;">💕</div>
<div class="fall" style="left: 55%; animation-delay: 0.5s;">💘</div>
<div class="fall" style="left: 70%; animation-delay: 1.5s;">💞</div>
<div class="fall" style="left: 85%; animation-delay: 2.5s;">💓</div>


""", unsafe_allow_html=True)

# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "no_btn_pos" not in st.session_state:
    st.session_state.no_btn_pos = random.randint(1, 1000000)

if "accepted" not in st.session_state:
    st.session_state.accepted = False

if "proposal_yes" not in st.session_state:
    st.session_state.proposal_yes = False

if "gift_reveal" not in st.session_state:
    st.session_state.gift_reveal = [False] * 3

# -----------------------------
# PASSWORD LOCK
# -----------------------------
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align:center;color:#ff2e7a;'>🔐 Private Surprise 💖</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:center;color:#ff69b4;'>Only for {GF_NAME} 😘</h3>", unsafe_allow_html=True)
    st.write("---")

    st.markdown("<div class='val_card'>", unsafe_allow_html=True)
    pass_input = st.text_input("Enter Password ❤️", type="password")
    if st.button("Unlock 💘"):
        if pass_input == SECRET_PASSWORD:
            st.session_state.logged_in = True
            st.success(f"Unlocked ✅ Welcome {GF_NAME} 💖")
            time.sleep(0.7)
            st.rerun()
        else:
            st.error(f"Wrong Password 😭 Try again {GF_NAME} 😘")
    st.markdown("</div>", unsafe_allow_html=True)

    st.stop()

# -----------------------------
# TOP LOGO TITLE
# -----------------------------
st.markdown(f"""
<div style="text-align:center;">
    <h1 style="color:#ff2e7a; font-size:46px;">{YOUR_NAME} ❤️ {GF_NAME}</h1>
    <p style="font-size:18px; color:#ff69b4;"><b>My Valentine Surprise Website 💘</b></p>
</div>
""", unsafe_allow_html=True)

st.write("---")

# -----------------------------
# MUSIC
# -----------------------------
st.markdown("<div class='val_card'>", unsafe_allow_html=True)

st.markdown("## 🎶 Play This Song (For You ❤️)")
st.caption("Song: Dooro Dooro")

audio_path = "music/dooro_dooro.mp3"

if os.path.exists(audio_path):
    audio_bytes = open(audio_path, "rb").read()
    st.audio(audio_bytes, format="audio/mp3")
else:
    st.warning("🎶 Song file missing! Upload: music/dooro_dooro.mp3")

st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# COUNTDOWN
# -----------------------------
today = date.today()
days_since_meet = (today - FIRST_MEET_DATE).days
days_since_relation = (today - RELATIONSHIP_DATE).days

st.markdown("<div class='val_card'>", unsafe_allow_html=True)
st.markdown("## ⏳ Our Love Countdown")
colA, colB = st.columns(2)
with colA:
    st.metric("Days since we met 💞", f"{days_since_meet} days")
with colB:
    st.metric("Days together ❤️", f"{days_since_relation} days")
st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

# -----------------------------
# LOVE LETTER
# -----------------------------
st.markdown("<div class='val_card'>", unsafe_allow_html=True)
st.markdown("## 💌 Hidden Love Letter")
with st.expander("Open My Love Letter 💖"):
    st.markdown(
        f"""
        Dear **{GF_NAME}** ❤️  

        You are my favorite person, my peace, my happiness ✨  
        Your smile is my safe place.  

        I promise to:
        - Love you endlessly 💞  
        - Always respect you 🌹  
        - Be with you in every situation 🤝  

        **Happy Valentine’s Day My Love 💖**  
        Forever Yours,  
        **{YOUR_NAME}** 😘
        """
    )
st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

# -----------------------------
# 100 REASONS
# -----------------------------
reasons = [
    "Your smile ❤️", "Your eyes 😍", "You understand me 🥺", "Your cute anger 😤💕",
    "You make me feel lucky 🍀", "You are my peace ✨", "Your voice feels like home 🏡",
    "You care about me 💖", "You’re my best friend 🤝", "You’re my everything 💘",
    "You make me laugh 😂", "You are beautiful 🌸", "You support me 💪",
    "You make my heart skip beats 💓", "You are my forever ♾️"
]

st.markdown("<div class='val_card'>", unsafe_allow_html=True)
st.markdown("## 🌹 100 Reasons I Love You")
if st.button("Generate a Reason 💞"):
    st.success(random.choice(reasons))
st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

# -----------------------------
# FIREWORKS
# -----------------------------
st.markdown("<div class='val_card'>", unsafe_allow_html=True)
st.markdown("## 🎇 Fireworks for You")
st.image("https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

# -----------------------------
# MAIN QUESTION
# -----------------------------
st.markdown("<div class='val_card'>", unsafe_allow_html=True)
st.markdown(
    f"<h2 style='text-align:center;color:#ff1493;'>Will you be my Valentine, {GF_NAME}? 💖</h2>",
    unsafe_allow_html=True
)

if st.session_state.accepted:
    st.balloons()
    st.success(f"YAAAYYY 😍❤️ {GF_NAME}, I LOVE YOUUUU 💕")

    st.markdown(
        f"""
        <h1 style="text-align:center;color:#ff2e7a;">😘 {GF_NAME} you made my day ❤️</h1>
        <h3 style="text-align:center;">Forever yours 💍✨</h3>
        <h3 style="text-align:center;color:#ff69b4;">— {YOUR_NAME}</h3>
        """,
        unsafe_allow_html=True
    )

   st.write("---")
st.markdown("## 🎞️ Photo Slideshow 💕")

img_folder = "images"
if os.path.exists(img_folder):
    all_imgs = sorted([f for f in os.listdir(img_folder) if f.lower().endswith((".jpg",".jpeg",".png"))])

    if len(all_imgs) > 0:
        slide = st.empty()
        for img in all_imgs:
            slide.image(os.path.join(img_folder, img), use_container_width=True)
            time.sleep(2)
    else:
        st.warning("No images found for slideshow.")
else:
    st.warning("images folder missing!")


    cols = st.columns(4)
    for i in range(4):
        with cols[i]:
            st.image(photos[i], use_container_width=True)

    st.image("https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif", use_container_width=True)
    st.stop()

col_yes, col_no = st.columns(2)

with col_yes:
    if st.button("✅ YES 💕"):
        st.session_state.accepted = True
        st.rerun()

with col_no:
    if st.button("❌ NO 😭", key=f"no_{st.session_state.no_btn_pos}"):
        st.session_state.no_btn_pos = random.randint(1, 1000000)
        st.warning("😈 NO option bhaag gaya hahaha... Try again Kittu 😘")
        time.sleep(0.5)
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)



