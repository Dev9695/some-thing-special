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
# HELPERS
# -----------------------------
def file_exists(path: str) -> bool:
    return os.path.exists(path) and os.path.isfile(path)

def list_images(folder="images"):
    if not os.path.exists(folder):
        return []
    exts = (".jpg", ".jpeg", ".png", ".webp")
    files = [f for f in os.listdir(folder) if f.lower().endswith(exts)]
    files.sort()
    return [os.path.join(folder, f) for f in files]

# -----------------------------
# CSS (BLACK TEXT + BLUR + HEART SNOW)
# -----------------------------
st.markdown("""
<style>
/* Force BLACK text everywhere */
* {
    color: #000000 !important;
}

/* Background */
.stApp {
    background: linear-gradient(180deg, #ffe6f0 0%, #fff0f5 60%, #ffffff 100%);
}

/* Inputs + labels */
label, p, span, div {
    color: #000000 !important;
}

/* Button text */
.stButton button {
    color: #000000 !important;
    background: rgba(255,255,255,0.9) !important;
    border-radius: 18px !important;
    padding: 10px 22px !important;
    font-size: 18px !important;
    font-weight: 800 !important;
    border: 1px solid rgba(0,0,0,0.1) !important;
    transition: 0.2s ease-in-out;
}
.stButton button:hover {
    transform: scale(1.05);
}

/* Glass card */
.val_card {
    background: rgba(255,255,255,0.65);
    border-radius: 20px;
    padding: 18px;
    box-shadow: 0px 8px 20px rgba(255, 0, 100, 0.15);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.45);
}

/* Heart snowfall */
.fall {
  position: fixed;
  top: -20px;
  animation: fallDown 7s linear infinite;
  font-size: 22px;
  opacity: 0.75;
  z-index: 0;
}
@keyframes fallDown {
  0% {transform: translateY(0);}
  100% {transform: translateY(120vh);}
}
</style>

<div class="fall" style="left: 10%; animation-delay: 0s;">💖</div>
<div class="fall" style="left: 25%; animation-delay: 1s;">💗</div>
<div class="fall" style="left: 40%; animation-delay: 2s;">💕</div>
<div class="fall" style="left: 55%; animation-delay: 0.5s;">💘</div>
<div class="fall" style="left: 70%; animation-delay: 1.5s;">💞</div>
<div class="fall" style="left: 85%; animation-delay: 2.5s;">💓</div>
""", unsafe_allow_html=True)

# -----------------------------
# SESSION STATE
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "accepted" not in st.session_state:
    st.session_state.accepted = False

if "no_btn_pos" not in st.session_state:
    st.session_state.no_btn_pos = random.randint(1, 999999)

# -----------------------------
# PASSWORD SCREEN
# -----------------------------
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align:center;'>🔐 Private Surprise 💖</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:center;'>Only for {GF_NAME} 😘</h3>", unsafe_allow_html=True)
    st.write("---")

    st.markdown("<div class='val_card'>", unsafe_allow_html=True)
    pwd = st.text_input("Enter Password ❤️", type="password")
    if st.button("Unlock 💘"):
        if pwd == SECRET_PASSWORD:
            st.session_state.logged_in = True
            st.success("Unlocked ✅")
            time.sleep(0.7)
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
    <h1 style="font-size:46px;">{YOUR_NAME} ❤️ {GF_NAME}</h1>
    <p style="font-size:18px;"><b>My Valentine Surprise Website 💘</b></p>
</div>
""", unsafe_allow_html=True)

st.write("---")

# -----------------------------
# MUSIC (FIXED)
# -----------------------------
st.markdown("<div class='val_card'>", unsafe_allow_html=True)
st.markdown("## 🎶 Play This Song (For You ❤️)")
st.caption("Song: Dooro Dooro")

audio_path = os.path.join("music", "dooro_dooro.mp3")

# Debug info (optional but helpful)
# st.write("Audio path:", audio_path)

if file_exists(audio_path):
    audio_bytes = open(audio_path, "rb").read()
    st.audio(audio_bytes, format="audio/mp3")
else:
    st.error("❌ Music file not found in repo!")
    st.info("✅ Fix: upload file at -> music/dooro_dooro.mp3")
st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

# -----------------------------
# COUNTDOWN
# -----------------------------
today = date.today()
st.markdown("<div class='val_card'>", unsafe_allow_html=True)
st.markdown("## ⏳ Our Love Counter")

c1, c2 = st.columns(2)
with c1:
    st.metric("Days since we met 💞", (today - FIRST_MEET_DATE).days)
with c2:
    st.metric("Days together ❤️", (today - RELATIONSHIP_DATE).days)

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

You are my favorite person ✨  
Your smile is my peace 😘  

Happy Valentine’s Day 💘  
Forever Yours,  
**{YOUR_NAME}** ❤️
""")

st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

# -----------------------------
# QUESTION
# -----------------------------
st.markdown("<div class='val_card'>", unsafe_allow_html=True)
st.markdown(
    f"<h2 style='text-align:center;'>Will you be my Valentine, {GF_NAME}? 💖</h2>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    if st.button("✅ YES 💕"):
        st.session_state.accepted = True
        st.rerun()

with col2:
    if st.button("❌ NO 😭", key=f"no_{st.session_state.no_btn_pos}"):
        st.session_state.no_btn_pos = random.randint(1, 999999)
        st.warning("😜 NO button bhaag gaya hahaha!")

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# AFTER YES
# -----------------------------
if st.session_state.accepted:
    st.balloons()
    st.success(f"YAYYY 😍❤️ {GF_NAME}, I LOVE YOUUU 💞")

    st.write("---")
    st.markdown("## 🖼️ Our Photos 💕")

    imgs = list_images("images")

    if len(imgs) == 0:
        st.error("❌ Photos not found!")
        st.info("✅ Fix: upload photos inside -> images/ folder (jpg/jpeg/png)")
    else:
        # Grid Gallery
        cols = st.columns(3)
        for i, img_path in enumerate(imgs):
            with cols[i % 3]:
                st.image(img_path, use_container_width=True)

        st.write("---")
        st.markdown("## 🎞️ Photo Slideshow 💞")

        slide = st.empty()
        for _ in range(2):  # slideshow repeat 2 times
            for img_path in imgs:
                slide.image(img_path, use_container_width=True)
                time.sleep(2)

    st.write("---")
    st.image("https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif", use_container_width=True)
