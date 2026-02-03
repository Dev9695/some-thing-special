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
# CSS + THEME + HEART SNOWFALL
# -----------------------------
st.markdown("""
<style>
html, body, [class*="css"] {
    color: black !important;
}

/* Background */
.stApp {
    background: linear-gradient(180deg, #ffe6f0 0%, #fff0f5 60%, #ffffff 100%);
}

/* Glass Card */
.val_card {
    background: rgba(255,255,255,0.65);
    border-radius: 20px;
    padding: 18px;
    box-shadow: 0px 8px 20px rgba(255, 0, 100, 0.15);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.45);
}

/* Buttons */
.stButton button {
    border-radius: 18px;
    padding: 10px 22px;
    font-size: 18px;
    font-weight: bold;
}

/* Heart snowfall */
.fall {
  position: fixed;
  top: -20px;
  animation: fallDown 8s linear infinite;
  font-size: 22px;
  opacity: 0.75;
}
@keyframes fallDown {
  0% {transform: translateY(0);}
  100% {transform: translateY(110vh);}
}
</style>

<div class="fall" style="left:10%;animation-delay:0s;">💖</div>
<div class="fall" style="left:25%;animation-delay:1s;">💗</div>
<div class="fall" style="left:40%;animation-delay:2s;">💕</div>
<div class="fall" style="left:55%;animation-delay:0.5s;">💘</div>
<div class="fall" style="left:70%;animation-delay:1.5s;">💞</div>
<div class="fall" style="left:85%;animation-delay:2.5s;">💓</div>
""", unsafe_allow_html=True)

# -----------------------------
# SESSION STATE
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "accepted" not in st.session_state:
    st.session_state.accepted = False

if "no_btn_pos" not in st.session_state:
    st.session_state.no_btn_pos = random.randint(1, 100000)

# -----------------------------
# PASSWORD SCREEN
# -----------------------------
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align:center;'>🔐 Private Surprise 💖</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:center;'>Only for {GF_NAME} 😘</h3>", unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='val_card'>", unsafe_allow_html=True)
        pwd = st.text_input("Enter Password ❤️", type="password")
        if st.button("Unlock 💘"):
            if pwd == SECRET_PASSWORD:
                st.session_state.logged_in = True
                st.success("Unlocked 💖")
                time.sleep(0.8)
                st.rerun()
            else:
                st.error("Wrong password 😅")
        st.markdown("</div>", unsafe_allow_html=True)

    st.stop()

# -----------------------------
# HEADER
# -----------------------------
st.markdown(f"""
<div style="text-align:center;">
<h1>{YOUR_NAME} ❤️ {GF_NAME}</h1>
<p><b>My Valentine Surprise Website 💘</b></p>
</div>
""", unsafe_allow_html=True)

st.write("---")

# -----------------------------
# MUSIC (FIXED)
# -----------------------------
st.markdown("<div class='val_card'>", unsafe_allow_html=True)
st.markdown("## 🎶 Play This Song (For You ❤️)")
st.caption("Song: Dooro Dooro")

audio_path = "music/dooro_dooro.mp3"
if os.path.exists(audio_path):
    st.audio(open(audio_path, "rb").read(), format="audio/mp3")
else:
    st.error("❌ music/dooro_dooro.mp3 not found")

st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

# -----------------------------
# COUNTDOWN
# -----------------------------
today = date.today()
st.markdown("<div class='val_card'>", unsafe_allow_html=True)
st.markdown("## ⏳ Our Love Counter")
c1, c2 = st.columns(2)
c1.metric("Days since we met 💞", (today - FIRST_MEET_DATE).days)
c2.metric("Days together ❤️", (today - RELATIONSHIP_DATE).days)
st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

# -----------------------------
# LOVE LETTER
# -----------------------------
st.markdown("<div class='val_card'>", unsafe_allow_html=True)
st.markdown("## 💌 Hidden Love Letter")
with st.expander("Open my letter 💖"):
    st.markdown(f"""
Dear **{GF_NAME}** ❤️  

You are my peace, my smile, my home.  
Every moment with you is special.

Forever yours,  
**{YOUR_NAME}** 😘
""")
st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

# -----------------------------
# VALENTINE QUESTION
# -----------------------------
st.markdown("<div class='val_card'>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align:center;'>Will you be my Valentine, {GF_NAME}? 💖</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("✅ YES 💕"):
        st.session_state.accepted = True
        st.rerun()

with col2:
    if st.button("❌ NO 😭", key=st.session_state.no_btn_pos):
        st.session_state.no_btn_pos = random.randint(1, 100000)
        st.warning("😜 NO button bhaag gaya!")

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# AFTER YES
# -----------------------------
if st.session_state.accepted:
    st.balloons()
    st.success("YAYYY ❤️ I LOVE YOU 💕")

    st.markdown("## 🖼️ Our Memories 💞")

    img_folder = "images"
    if os.path.exists(img_folder):
        imgs = [f for f in os.listdir(img_folder) if f.lower().endswith((".jpg",".jpeg",".png"))]
        cols = st.columns(3)
        for i, img in enumerate(imgs):
            with cols[i % 3]:
                st.image(os.path.join(img_folder, img), use_container_width=True)

        st.write("---")
        st.markdown("## 🎞️ Photo Slideshow")
        slide = st.empty()
        for img in imgs:
            slide.image(os.path.join(img_folder, img), use_container_width=True)
            time.sleep(2)
    else:
        st.warning("Images folder missing")

    st.image("https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif", use_container_width=True)
