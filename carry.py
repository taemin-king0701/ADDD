import streamlit as st

# --- 페이지 기본 설정 (Preserving layout) ---
st.set_page_config(page_title="원딜 위키", page_icon="🎯", layout="centered")

# --- 세션 상태 초기화 (페이지 이동 마술을 위한 장치) ---
if 'page' not in st.session_state:
    st.session_state.page = 'home' # home, list, detail 3가지 상태로 관리
if 'selected_champ' not in st.session_state:
    st.session_state.selected_champ = None

# --- 페이지 이동 함수들 (No changes) ---
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
    
    # [수정 사항] 챔피언 목록 및 로컬 이미지 파일 매핑
    champions = [
        "드레이븐", "유나라", "미스 포츈", "이즈리얼", "카이사", 
        "아펠리오스", "자야", "코르키", "케이틀린", "루시안", 
        "칼리스타", "애쉬", "코그모", "진", "제리", 
        "징크스", "바루스", "시비르"
    ]
    sorted_champs = sorted(champions)

    # 로컬 이미지 파일 매핑 (제공된 파일 이름)
    # **중요**: image_0.png(드레이븐)와 image_1.png(바루스) 파일이 
    # **app.py와 같은 폴더**에 있어야 합니다.
    local_images = {
        "드레이븐": "image_0.png",
        "바루스": "image_1.png"
    }
    
    # [수정 사항] 리스트 출력 시 로컬 이미지 및 플레이스홀더 적용
    for champ in sorted_champs:
        # 화면을 2개의 구역으로 나눔 (비율 1:4)
        col1, col2 = st.columns([1, 4])
        
        with col1:
            # 챔피언별 로컬 이미지 혹은 플레이스홀더
            image_file = local_images.get(champ) # 매핑된 파일명 가져오기
            
            # (핵심) 파일을 직접 사용하여 오류 방지 및 출력
            try:
                if image_file:
                    # 파일 이름을 직접 사용하여 로드
                    st.image(image_file, width=80, caption=f"{champ} 초상화") 
                else:
                    # 파일이 없는 다른 챔피언은 심플한 로컬 플레이스홀더 (회색 박스)
                    st.markdown("<div style='width:80px;height:80px;background-color:#eee;border-radius:10px;text-align:center;line-height:80px;color:#888;'>🖼️ 준비중</div>", unsafe_allow_html=True)
            except FileNotFoundError:
                # 파일 위치 문제 해결 유도
                st.write(f"🚫 {image_file} 파일 없음") 
            except Exception as e:
                # 기타 예기치 않은 오류 처리
                st.write(f"⚠️ {champ} 로드 실패: {e}")
            
        with col2:
            # 수직 정렬을 위해 약간의 여백 추가
            st.write("") 
            # 클릭 시 해당 챔피언의 공략 페이지로 이동하는 버튼 (키 값 고유화)
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
    
    # [참고] Detail 페이지의 배너는 여전히 플레이스홀더입니다.
    # 나중에 큰 배너 파일들을 넣어 배너 코드를 st.image("로컬파일.png")로 바꾸면 됩니다.
    st.image("https://via.placeholder.com/800x250?text=Detail+Placeholder", use_container_width=True)
    
    st.subheader("📝 챔피언 특징 및 장인들의 비급")
    st.write(f"이곳은 오직 **{champ}**만을 위한 신성한 공간이야.")
    st.write("라인전 날먹하는 법부터 한타 때 상대 암살자 농락하는 무빙까지 차근차근 적어보자구!")
    
    # 나중에 여기에 입력창(st.text_area)이나 마크다운으로 공략을 길게 적으면 됨
    st.info("🚧 현재 절찬리에 공략 작성 중 🚧")
    
    st.write("---")
    st.button("⬅️ 챔피언 목록으로 돌아가기", on_click=go_back_to_list)
