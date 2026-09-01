import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="원딜 위키", page_icon="🎯", layout="centered")

# 챔피언 한글명 -> 초상화 URL (Community Dragon CDN, "latest" 경로라 버전 관리 불필요)
CHAMPION_IMAGE_MAP = {
    "드레이븐": "https://cdn.communitydragon.org/latest/champion/Draven/square",
    "미스 포츈": "https://cdn.communitydragon.org/latest/champion/MissFortune/square",
    "이즈리얼": "https://cdn.communitydragon.org/latest/champion/Ezreal/square",
    "카이사": "https://cdn.communitydragon.org/latest/champion/Kaisa/square",
    "아펠리오스": "https://cdn.communitydragon.org/latest/champion/Aphelios/square",
    "자야": "https://cdn.communitydragon.org/latest/champion/Xayah/square",
    "코르키": "https://cdn.communitydragon.org/latest/champion/Corki/square",
    "케이틀린": "https://cdn.communitydragon.org/latest/champion/Caitlyn/square",
    "루시안": "https://cdn.communitydragon.org/latest/champion/Lucian/square",
    "칼리스타": "https://cdn.communitydragon.org/latest/champion/Kalista/square",
    "애쉬": "https://cdn.communitydragon.org/latest/champion/Ashe/square",
    "코그모": "https://cdn.communitydragon.org/latest/champion/KogMaw/square",
    "진": "https://cdn.communitydragon.org/latest/champion/Jhin/square",
    "제리": "https://cdn.communitydragon.org/latest/champion/Zeri/square",
    "징크스": "https://cdn.communitydragon.org/latest/champion/Jinx/square",
    "바루스": "https://cdn.communitydragon.org/latest/champion/Varus/square",
    "시비르": "https://cdn.communitydragon.org/latest/champion/Sivir/square",
    # "유나라"는 정확히 매칭되는 챔피언을 확인 못해 일단 제외했어요.
    # 실제 챔피언명을 알려주면 바로 추가해드릴게요.
}


def get_champion_image_url(champ_name):
    return CHAMPION_IMAGE_MAP.get(champ_name)


# 세션 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = "intro"  # intro / list / detail
if "selected_champ" not in st.session_state:
    st.session_state.selected_champ = None


def enter_wiki():
    st.session_state.page = "list"


def go_to_detail(champ):
    st.session_state.selected_champ = champ
    st.session_state.page = "detail"


def back_to_list():
    st.session_state.selected_champ = None
    st.session_state.page = "list"


def back_to_intro():
    st.session_state.page = "intro"


# 1. 첫 화면
if st.session_state.page == "intro":
    st.markdown(
        "<h1 style='text-align: center; color: #FF4B4B;'>캐리를 하고 싶은 자들을 위한 위키</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h3 style='text-align: center;'>숟가락이라는 멸칭은 잊어라! 우리가 바로 게임의 주인공이다! 🥄✨</h3>",
        unsafe_allow_html=True,
    )
    st.write("---")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.button(
            "들어가기 🚀 (클릭 시 마우스 우클릭 연타 준비)",
            on_click=enter_wiki,
            use_container_width=True,
        )

# 2. 챔피언 목록 화면
elif st.session_state.page == "list":
    st.title("원거리 딜러 챔피언 도감 🎯")
    st.write("가나다 순으로 예쁘게 정렬해 놨어. 이제 카이팅 연습만 남았다!")
    st.write("---")

    champions = [
        "드레이븐", "유나라", "미스 포츈", "이즈리얼", "카이사",
        "아펠리오스", "자야", "코르키", "케이틀린", "루시안",
        "칼리스타", "애쉬", "코그모", "진", "제리",
        "징크스", "바루스", "시비르",
    ]
    sorted_champs = sorted(champions)

    # 초상화 + 버튼을 3열 그리드로 배치
    cols_per_row = 3
    for i in range(0, len(sorted_champs), cols_per_row):
        row_champs = sorted_champs[i : i + cols_per_row]
        row_cols = st.columns(cols_per_row)
        for col, champ in zip(row_cols, row_champs):
            with col:
                img_url = get_champion_image_url(champ)
                if img_url:
                    st.image(img_url, use_container_width=True)
                else:
                    st.markdown(
                        "<div style='height:80px; display:flex; align-items:center; "
                        "justify-content:center; background:#333; border-radius:8px; "
                        "color:white;'>🎯</div>",
                        unsafe_allow_html=True,
                    )
                st.button(
                    champ,
                    key=f"btn_{champ}",
                    on_click=go_to_detail,
                    args=(champ,),
                    use_container_width=True,
                )

    st.write("---")
    st.button("⬅️ 뒤로 가기 (우물로 귀환)", on_click=back_to_intro)

# 3. 챔피언 상세 화면
elif st.session_state.page == "detail":
    champ = st.session_state.selected_champ
    img_url = get_champion_image_url(champ)

    col1, col2 = st.columns([1, 3])
    with col1:
        if img_url:
            st.image(img_url, use_container_width=True)
    with col2:
        st.title(champ)

    st.write("---")
    st.write(
        f"여기에 **{champ}**의 카이팅 비법과 서포터에게 핑 찍는(?) 노하우를 "
        "적을 예정입니다. (현재 공사 중 🚧)"
    )

    st.write("---")
    st.button("⬅️ 목록으로 돌아가기", on_click=back_to_list)
