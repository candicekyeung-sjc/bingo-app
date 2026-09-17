import streamlit as st
import random
from PIL import Image

# --- Word list with image paths ---
words_with_images = {
    "耶穌": "images/jesus.png",
    "聖母": "images/mary.png",
    "方舟": "images/ark.png",
    "十誡": "images/commandments.png",
    "聖堂": "images/church.png",
    "祈禱": "images/prayer.png",
    "聖詠": "images/psalm.png",
    "伯多祿": "images/peter.png",
    "聖猶達": "images/jude.png",
    "五餅二魚": "images/loaves_fishes.png",
    "復活": "images/resurrection.png",
    "牧羊人": "images/shepherd.png",
    "天國": "images/heaven.png",
    "鴿子": "images/dove.png",
    "十字架": "images/cross.png",
    "種子": "images/seed.png",
    "好撒瑪黎雅人": "images/samaritan.png",
    "最後晚餐": "images/lastsupper.png",
    "葡萄樹": "images/vine.png",
    "彩虹": "images/rainbow.png",
    "天使": "images/angel.png",
    "婚宴": "images/wedding.png",
    "聖經": "images/bible.png",
    "聖神": "images/holyspirit.png"
}

# --- Session state ---
if "draws" not in st.session_state:
    st.session_state.draws = random.sample(list(words_with_images.keys()), len(words_with_images))
    st.session_state.index = 0
    st.session_state.history = []

st.title("主內團圓慶中秋 BINGO")

# --- Layout with 4 columns ---
col1, col2, col3, col4 = st.columns([1,1,3,1])  # left, middle, right

# Left column → History
with col1:
    st.subheader("History")
    st.markdown(
        f"<p style='font-size:20px;'> {' → '.join(st.session_state.history)} </p>",
        unsafe_allow_html=True
    )

# Middle column → Next Word button + Current word + image
with col3:
    # Button first
    if st.button("Next Word"):
        if st.session_state.index < len(st.session_state.draws):
            word = st.session_state.draws[st.session_state.index]
            st.session_state.history.append(word)
            st.session_state.index += 1
        else:
            st.session_state.history.append("🎉 所有圖案已經顯示 All words called!")

    # Then show word + image
    if st.session_state.history:
        current_word = st.session_state.history[-1]
        st.markdown(
            f"<h1 style='text-align:center; color:darkred; font-size:68px;'> {current_word} </h1>",
            unsafe_allow_html=True
        )
        img_path = words_with_images.get(current_word)
        if img_path and "All words" not in current_word:
            try:
                st.image(img_path, width=400)
            except:
                st.write("(所有圖案已經顯示 No image available)")

# Right column → Reset button
with col4:
    if st.button("Reset Game"):
        st.session_state.draws = random.sample(list(words_with_images.keys()), len(words_with_images))
        st.session_state.index = 0
        st.session_state.history = []

