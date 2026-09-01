import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="원딜 위키", page_icon="🎯", layout="centered")

# 라이엇 공식 이미지 서버(Data Dragon) 연결을 위한 영문명 매핑
champ_eng = {
    "드레이븐": "Draven", "미스 포츈": "MissFortune", "이즈리얼": "Ezreal",
    "카이사": "Kaisa", "아펠리오스": "Aphelios", "자야": "Xayah",
    "코르키": "Corki", "케이틀린": "Caitlyn", "루시안": "Lucian",
    "칼리스타": "Kalista", "애쉬": "Ashe", "코그모": "KogMaw",
    "진": "Jhin", "제리": "Zeri", "징크스": "Jinx",
    "바루스": "Varus", "시비르": "Sivir", 
    "유나라": "Teemo" # 유나라는 정체불명이라 일단 티모로 박제!
}

# --- 세션 상태 초기화 ---
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'selected_champ' not in st.session_state:
    st.session_state.selected_champ = None

# --- 페이지 이동 함수 ---
def go_to_list(): st.session_state.page = 'list'
def go_to_champ(champ_name):
    st.session_state.page = 'detail'
    st.session_state.selected_champ = champ_name
def go_back_to_list(): st.session_state.page = 'list'
def go_to_home(): st.session_state.page = 'home'

# ==========================================
# 1. 첫 화면 (Home)
# ==========================================
if st.session_state.page == 'home':
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>캐리를 하고 싶은 자들을 위한 위키</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>대포 미니언을 놓친 자, 이 곳에 들어올 자격이 없다! 🥄✨</h3>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.button("들어가기 🚀", on_click=go_to_list, use_container_width=True)

# ==========================================
# 2. 챔피언 목록 화면 (List)
# ==========================================
elif st.session_state.page == 'list':
    st.title("원거리 딜러 챔피언 도감 🎯")
    st.write("가나다 순으로 정렬 완료! 이제 공략만 채우면 완벽해.")
    st.write("---")
    
    sorted_champs = sorted(list(champ_eng.keys()))
    
    for champ in sorted_champs:
        col1, col2 = st.columns([1, 4])
        
        with col1:
            # 라이엇 서버에서 챔피언 아이콘 직접 불러오기
            eng_name = champ_eng.get(champ, "Teemo")
            icon_url = f"https://ddragon.leagueoflegends.com/cdn/14.4.1/img/champion/{eng_name}.png"
            st.image(icon_url, width=80)
            
        with col2:
            st.write("") 
            st.button(f"{champ} 공략 보러가기 ⚔️", key=f"btn_{champ}", on_click=go_to_champ, args=(champ,))
            
        st.write("---")
        
    if st.button("⬅️ 우물로 귀환 (첫 화면으로)"):
        go_to_home()

# ==========================================
# 3. 챔피언 개별 공략 화면 (Detail)
# ==========================================
elif st.session_state.page == 'detail':
    champ = st.session_state.selected_champ
    eng_name = champ_eng.get(champ, "Teemo")
    
    st.title(f"👑 {champ} 집중 탐구")
    
    # 라이엇 서버에서 챔피언 고화질 배경 일러스트 불러오기
    splash_url = f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{eng_name}_0.jpg"
    st.image(splash_url, use_container_width=True)
    
    st.subheader("📝 챔피언 특징 및 장인들의 비급")
    st.write(f"**{champ}**의 카이팅 비법과 서포터 멘탈 터뜨리는 노하우를 적어보자!")
    
    st.text_area("여기에 공략을 마구마구 적어주세요!", height=200)
    
    st.write("---")
    st.button("⬅️ 챔피언 목록으로 돌아가기", on_click=go_back_to_list)
