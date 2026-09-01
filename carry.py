import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="원딜 위키", page_icon="🎯", layout="centered")

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

# 라이엇 서버에서 얼굴만 나오는 타일(Tile) 이미지를 가져오기 위한 영문명
champ_eng = {
    "드레이븐": "Draven", "미스 포츈": "MissFortune", "이즈리얼": "Ezreal",
    "카이사": "Kaisa", "아펠리오스": "Aphelios", "자야": "Xayah",
    "코르키": "Corki", "케이틀린": "Caitlyn", "루시안": "Lucian",
    "칼리스타": "Kalista", "애쉬": "Ashe", "코그모": "KogMaw",
    "진": "Jhin", "제리": "Zeri", "징크스": "Jinx",
    "바루스": "Varus", "시비르": "Sivir", 
    "유나라": "Teemo" # 여전히 정체불명이라 웃음벨 티모로 유지!
}

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
    st.write("가나다 순으로 정렬 완료! 이제 सीएस(CS) 먹듯 공략을 채워봐.")
    st.write("---")
    
    sorted_champs = sorted(list(champ_eng.keys()))
    
    for champ in sorted_champs:
        col1, col2 = st.columns([1, 4])
        
        with col1:
            # 버전 업데이트에 영향받지 않는 영구적인 얼굴 썸네일(Tile) 주소 사용
            eng_name = champ_eng.get(champ)
            tile_url = f"https://ddragon.leagueoflegends.com/cdn/img/champion/tiles/{eng_name}_0.jpg"
            st.image(tile_url, width=80)
            
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
    eng_name = champ_eng.get(champ)
    
    st.title(f"👑 {champ} 집중 탐구")
    
    # 디테일 페이지는 웅장한 가로 배경 일러스트 유지
    splash_url = f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{eng_name}_0.jpg"
    st.image(splash_url, use_container_width=True)
    
    st.subheader("📝 챔피언 특징 및 장인들의 비급")
    st.write(f"**{champ}**의 피지컬 뽐내는 법과 암살자 대처법을 낱낱이 파헤쳐보자!")
    
    st.info("🚧 현재 절찬리에 공략 작성 중 🚧")
    
    st.write("---")
    st.button("⬅️ 챔피언 목록으로 돌아가기", on_click=go_back_to_list)
