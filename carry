import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="원딜 위키", page_icon="🎯")

# 세션 상태 초기화 (첫 화면과 목록 화면 전환용)
if 'entered' not in st.session_state:
    st.session_state.entered = False

# 들어가기 버튼 클릭 시 실행될 함수
def enter_wiki():
    st.session_state.entered = True

# 1. 첫 화면
if not st.session_state.entered:
    # 제목을 크고 강렬하게!
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>캐리를 하고 싶은 자들을 위한 위키</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>숟가락이라는 멸칭은 잊어라! 우리가 바로 게임의 주인공이다! 🥄✨</h3>", unsafe_allow_html=True)
    st.write("---")
    
    # 버튼을 가운데로 정렬하기 위해 컬럼 사용
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.button("들어가기 🚀 (클릭 시 마우스 우클릭 연타 준비)", on_click=enter_wiki, use_container_width=True)

# 2. 챔피언 목록 화면
else:
    st.title("원거리 딜러 챔피언 도감 🎯")
    st.write("가나다 순으로 예쁘게 정렬해 놨어. 이제 카이팅 연습만 남았다!")
    st.write("---")
    
    # 알려준 챔피언 리스트
    champions = [
        "드레이븐", "유나라", "미스 포츈", "이즈리얼", "카이사", 
        "아펠리오스", "자야", "코르키", "케이틀린", "루시안", 
        "칼리스타", "애쉬", "코그모", "진", "제리", 
        "징크스", "바루스", "시비르"
    ]
    
    # 파이썬 내장 함수를 사용해 완벽하게 가나다 순으로 정렬
    sorted_champs = sorted(champions)
    
    # 정렬된 챔피언 목록 출력
    for champ in sorted_champs:
        # 나중에 특징과 공략법을 편하게 넣을 수 있도록 expander(접기/펴기) 기능 활용
        with st.expander(f"🔫 {champ}"):
            st.write(f"여기에 **{champ}**의 카이팅 비법과 서포터에게 핑 찍는(?) 노하우를 적을 예정입니다. (현재 공사 중 🚧)")
            
    st.write("---")
    
    # 다시 첫 화면으로 돌아가는 버튼 (우물로 귀환)
    if st.button("⬅️ 뒤로 가기 (우물로 귀환)"):
        st.session_state.entered = False
        st.rerun()
