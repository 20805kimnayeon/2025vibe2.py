import streamlit as st
import random
import base64
import os

# 페이지 설정
st.set_page_config(page_title="호주된 오리의 탈출!!!", page_icon="🐦", layout="centered")

# 배경 설정

def get_bg():
    img_path = "img/duck_bg.jpg"
    if os.path.exists(img_path):
        with open(img_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
            return f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{encoded}");
                background-size: cover;
                background-position: center;
                color: white;
            }}
            .title {{
                font-size: 48px;
                font-weight: bold;
                text-align: center;
                color: #ffe600;
                text-shadow: 2px 2px 4px #000000;
            }}
            .msg {{
                font-size: 22px;
                text-shadow: 1px 1px 2px #000000;
            }}
            </style>
            """
    else:
        return ""  # No background if image not found

st.markdown(get_bg(), unsafe_allow_html=True)

# 포인트 해제되는 결과와 이벤트들
rooms = [
    {
        "desc": "호주된 오리는 시험실에 가치되어 있습니다. 압류화 물이 기원화되는 것 같은 것도...",
        "choices": {
            "포탈을 터지고 돌아기": "지팡이를 담당한 것 같은 파이어의 힘에 매우치고 마주되었습니다... 😿",
            "문을 열기": "건조물이 내려와 위험한 전격복이 복당되었습니다! 지명 다루기... ☠️",
            "해외에서 잡으려 보는 타이다운": "성공적인 선택! 안전한 사무시에 도착! 🎉"
        }
    },
    {
        "desc": "다음 방에는 검색 로벌이 있습니다. 어디서든 복장을 하는 것 같은 곳입니다...",
        "choices": {
            "드레스를 우클릭하며 진입": "로벌이 해명에 감도해 여름 프리트 같은 협조를 얻었습니다! ✨",
            "숨다": "로벌이 복공하지 못했고, 자른 지각 안에 떨어진 오리가 다친 드레시를 드러버렸습니다. 🩸",
            "이벤트를 다룰다!": "다음 시카의 무엇인가요...? 많은 후효가 예감됩니다. 🕷️"
        }
    }
]

# 게임 진행 정보 저장
if 'room' not in st.session_state:
    st.session_state.room = 0
    st.session_state.history = []

# 게임 복귀
if st.button("🔄 최천의 설정버드로 다시 시작!"):
    st.session_state.room = 0
    st.session_state.history = []
    st.experimental_rerun()

# 현재 방 표시
if st.session_state.room < len(rooms):
    room = rooms[st.session_state.room]
    st.markdown(f"<div class='title'>🐦 오리흘 내림 이중... 🕵️</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='msg'>{room['desc']}</div>", unsafe_allow_html=True)

    for choice, result in room['choices'].items():
        if st.button(choice):
            st.session_state.history.append((choice, result))
            st.session_state.room += 1
            st.experimental_rerun()
else:
    st.markdown(f"<div class='title'>🎉 게임 종료! 결
