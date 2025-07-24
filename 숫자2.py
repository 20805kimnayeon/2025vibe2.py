import streamlit as st
import random
import base64

# 페이지 설정
st.set_page_config(page_title="🌈 숫자 맞히기 게임 폭탄 에디션", page_icon="🎯", layout="centered")

# 🔮 배경 이미지 설정
def set_fancy_background(image_path):
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }}
    .title {{
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: #ffeb3b;
        text-shadow: 3px 3px 6px #000000;
        padding: 10px;
    }}
    .subtitle {{
        font-size: 20px;
        text-align: center;
        color: #fff;
        text-shadow: 1px 1px 2px #000000;
    }}
    </style>
    """, unsafe_allow_html=True)

# 배경 설정
set_fancy_background("img/fancy_bg.png")

# 오디오 재생
def play_audio(path):
    audio_file = open(path, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')

# 🌈 타이틀
st.markdown('<div class="title">🎯 숫자 맞히기 게임 폭탄 에디션 🎯</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">✨숫자를 맞히고 이모지 보상을 받아보세요!✨</div>', unsafe_allow_html=True)
st.markdown("")

# 😎 난이도 선택
difficulty = st.radio("🎚️ 난이도를 골라주세요!", ["🍼 쉬움", "😬 보통", "🔥 어려움"])
if difficulty == "🍼 쉬움":
    max_num, max_tries = 50, 10
elif difficulty == "😬 보통":
    max_num, max_tries = 100, 7
else:
    max_num, max_tries = 200, 5

# 세션 상태 초기화
if 'target' not in st.session_state:
    st.session_state.target = random.randint(1, max_num)
    st.session_state.tries = 0
    st.session_state.game_over = False

# 📢 게임 설명
st.markdown(f"🎮 <b>1 ~ {max_num}</b> 사이 숫자를 맞혀보세요!", unsafe_allow_html=True)
st.markdown(f"💖 남은 기회: <b>{max_tries - st.session_state.tries}</b>번", unsafe_allow_html=True)

# 숫자 입력 받기
if not st.session_state.game_over:
    guess = st.number_input("🔢 숫자를 입력하세요!", min_value=1, max_value=max_num, step=1)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🎯 도전!"):
            st.session_state.tries += 1

            # 정답 반응
            if guess == st.session_state.target:
                play_audio("audio/correct.mp3")
                st.success("🎉🎊 정답입니다!!! 🎊🎉")
                st.balloons()
                st.markdown("🥳✨💎🌈🦄🌟🎁💖🍭🎂🍬")
                st.session_state.game_over = True

            # 오답 반응
            elif guess < st.session_state.target:
                play_audio("audio/wrong.mp3")
                st.warning("📉 숫자가 너무 작아요! ⬆️")
                st.markdown("🙈🔍🤔")
            else:
                play_audio("audio/wrong.mp3")
                st.warning("📈 숫자가 너무 커요! ⬇️")
                st.markdown("😰🥵🔍")

            # 실패 처리
            if st.session_state.tries >= max_tries and not st.session_state.game_over:
                st.error(f"💥 기회 소진! 정답은 **{st.session_state.target}** 였습니다.")
                st.markdown("😭💔😵😩👎")
                st.session_state.game_over = True

    with col2:
        if st.button("🔄 다시 시작!"):
            st.session_state.target = random.randint(1, max_num)
            st.session_state.tries = 0
            st.session_state.game_over = False
            play_audio("audio/start.mp3")
            st.experimental_rerun()

# 🎁 하단
if st.session_state.game_over:
    st.markdown("---")
    st.markdown("💫 다음 게임도 도전해 보세요! 💫")
    st.markdown("🎈✨🍀💥🎉🧁🌟💎🎮🧠")
