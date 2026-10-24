import streamlit as st
import random
from PIL import Image

# --- Word list with image paths ---
words_with_images = {
    "輔祭 Altar": "images/altar.png",
    "St. Andrew": "images/andrew.png",
    "天使 Angel": "images/angel.png",
    "St. Anthony": "images/anthony.png",
    "方舟 Ark": "images/ark.png",
    "文物室 Heritage Centre": "images/artifacts.png",
    "聖經 Bible": "images/bible.png",
    "茶座 Cafe": "images/cafe.png",
    "周守仁樞機 Cardinal": "images/cardinal.png",
    "聖物部 Religious Articles": "images/centre_RA.png",
    "顯容小堂 Chapel": "images/chapel.png",
    "歌詠團 Choir": "images/choir.png",
    "聖堂 Church": "images/church.png",
    "十誡 Commandments": "images/commandments.png",
    "十字架 Cross": "images/cross.png",
    "聖水池 Holy Water": "images/holy_water.png",
    "聖神 Holy Spirit": "images/holyspirit.png",
    "St. James the Great": "images/James_the_great.png",
    "St. James the Less": "images/James_the_less.png",
    "耶穌 Jesus": "images/jesus.png",
    "St. John": "images/john.png",
    "St. Jude": "images/jude.png",
    "最後晚餐 Last Supper": "images/lastsupper.png",
    "希望之光 Light of Hope": "images/light_of_hope.png",
    "五餅二魚 Loaves & Fishes": "images/loaves_fishes.png",
    "聖母 Mother Mary": "images/mary.png",
    "彌撒中心 Mass Centre": "images/mass_centre.png",
    "St. Matthew": "images/matthew.png",
    "St. Paul": "images/paul.png",
    "St. Peter": "images/peter.png",
    "St. Philip": "images/philip.png",
    "教宗 Pope": "images/pope.png",
    "祈禱 Pray": "images/prayer.png",
    "彩虹 Rainbow": "images/rainbow.png",
    "讀經員 Lector": "images/readers.png",
    "復活 Resurrection": "images/resurrection.png",
    "團聚 Reunion": "images/reunion.png",
    "宿霧聖嬰 Santo Nino": "images/santonino.png",
    "牧羊人 Shepherd": "images/shepherd.png",
    "St. Simon": "images/simon.png",
    "紀念品 Souvenir": "images/souvenir.png",
    "聖猶達堂 St. Jude's Church": "images/stjudeschurch.png",
    "St. Thomas": "images/thomas.png",
}

# --- Session state ---
if "draws" not in st.session_state:
    st.session_state.draws = random.sample(list(words_with_images.keys()), len(words_with_images))
    st.session_state.index = 0
    st.session_state.history = []

# --- Set page background colour ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #ffecd2, #fcb69f);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- Set page title ---
st.title("聖猶達堂慶祝建堂73周年主保瞻禮 BINGO")

# --- Layout with 4 columns ---
col1, col2, col3, col4 = st.columns([2,1,4,1])  # left, middle, right

# Left column → History
with col1:
    st.subheader("History")
    st.markdown(
        f"<p style='font-size:20px;'> {' → '.join(st.session_state.history)} </p>",
        unsafe_allow_html=True
    )

# Middle column → Current word + image
with col3:
   if st.session_state.history:
        current_word = st.session_state.history[-1]
        st.markdown(
            f"<h1 style='text-align:center; color:#fcb69f; font-size:18px;'> {current_word} </h1>",
            unsafe_allow_html=True
        )
        img_path = words_with_images.get(current_word)
        if img_path and "All words" not in current_word:
            try:
                st.image(img_path, width=600)
            except:
                st.write("(遊戲完畢 Game Ended!)")

# Right column → Next Word button
with col4:
    if st.button("Next Word"):
        if st.session_state.index < len(st.session_state.draws):
            word = st.session_state.draws[st.session_state.index]
            st.session_state.history.append(word)
            st.session_state.index += 1
        else:
            st.session_state.history.append("🎉 遊戲完畢 Game Ended!")

# Reset button at the bottom

if st.button("Reset Game"):
    st.session_state.draws = random.sample(list(words_with_images.keys()), len(words_with_images))
    st.session_state.index = 0
    st.session_state.history = []

