import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="원딜 위키", page_icon="🎯", layout="centered")

# --- 세션 상태 초기화 (페이지 이동 마술을 위한 장치) ---
if 'page' not in st.session_state:
    st.session_state.page = 'home' # home, list, detail 3가지 상태로 관리
if 'selected_champ' not in st.session_state:
    st.session_state.selected_champ = None

# --- 페이지 이동 함수들 ---
def go_to_list():
    st.session_state.page = 'list'

def go_to_champ(champ_name):
    st.session_state.page = 'detail'
    st.session_state.selected_champ = champ_name

def go_back_to_list():
    st.session_state.page = 'list'
    st.session_state.selected_champ = None

def go_to_home():
    st.session_state.page = 'home'

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
    st.write("가나다 순으로 완벽하게 정렬했어. 공략을 보고 싶은 챔피언을 선택해 봐!")
    st.write("---")
    
    champions = [
        "드레이븐", "유나라", "미스 포츈", "이즈리얼", "카이사", 
        "아펠리오스", "자야", "코르키", "케이틀린", "루시안", 
        "칼리스타", "애쉬", "코그모", "진", "제리", 
        "징크스", "바루스", "시비르"
    ]
    sorted_champs = sorted(champions)
    
    # 리스트 출력
    for champ in sorted_champs:
        # 화면을 2개의 구역으로 나눔 (비율 1:4)
        col1, col2 = st.columns([1, 4])
        
        with col1:
            # 임시 이미지 삽입 (챔피언 이름이 들어간 회색 네모)
            st.image(f"https://via.placeholder.com/100?text={champ}", width=80)
            
        with col2:
            # 수직 정렬을 위해 약간의 여백 추가
            st.write("") 
            # 클릭 시 해당 챔피언의 공략 페이지로 이동하는 버튼
            st.button(f"{champ} 공략 보러가기 ⚔️", key=f"btn_{champ}", on_click=go_to_champ, args=(champ,))
            
        st.write("---") # 구분선 추가
        
    if st.button("⬅️ 우물로 귀환 (첫 화면으로)"):
        go_to_home()

# ==========================================
# 3. 챔피언 개별 공략 화면 (Detail)
# ==========================================
elif st.session_state.page == 'detail':
    champ = st.session_state.selected_champ
    
    st.title(f"👑 {champ} 집중 탐구")
    
    # 챔피언별 큰 초상화 (임시 배너 이미지)
    st.image(f"https://via.placeholder.com/800x250?text={champ}+Mastery", use_container_width=True)
    
    st.subheader("📝 챔피언 특징 및 장인들의 비급")
    st.write(f"이곳은 오직 **{champ}**만을 위한 신성한 공간이야.")
    st.write("라인전 날먹하는 법부터 한타 때 상대 암살자 농락하는 무빙까지 차근차근 적어보자구!")
    
    # 나중에 여기에 입력창(st.text_area)이나 마크다운으로 공략을 길게 적으면 됨
    st.info("🚧 현재 절찬리에 공략 작성 중 🚧")
    
    st.write("---")
    st.button("⬅️ 챔피언 목록으로 돌아가기", on_click=go_back_to_list)
