import streamlit as st


# ---------------------------------------------------
# 페이지 기본 설정
# ---------------------------------------------------
st.set_page_config(
    page_title="방배중학교 소개",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------
# CSS 디자인
# ---------------------------------------------------
st.markdown(
    """
    <style>
        /* 전체 배경 */
        .stApp {
            background:
                linear-gradient(
                    135deg,
                    #f5f9ff 0%,
                    #ffffff 50%,
                    #f4fff8 100%
                );
        }

        /* 기본 글꼴 */
        html, body, [class*="css"] {
            font-family:
                "Pretendard",
                "Noto Sans KR",
                Arial,
                sans-serif;
        }

        /* 제목 영역 */
        .hero {
            padding: 55px 35px;
            border-radius: 25px;
            text-align: center;
            color: white;
            background:
                linear-gradient(
                    135deg,
                    #124e96 0%,
                    #2878c8 55%,
                    #30a46c 100%
                );
            box-shadow: 0 12px 30px rgba(0, 57, 115, 0.22);
            margin-bottom: 30px;
        }

        .hero-badge {
            display: inline-block;
            padding: 7px 17px;
            margin-bottom: 13px;
            border-radius: 20px;
            background: rgba(255, 255, 255, 0.18);
            font-size: 15px;
            font-weight: 700;
        }

        .hero h1 {
            margin: 0;
            font-size: 48px;
            font-weight: 900;
            letter-spacing: -2px;
        }

        .hero p {
            margin: 14px 0 0 0;
            font-size: 21px;
            font-weight: 500;
        }

        /* 카드 */
        .info-card {
            min-height: 175px;
            padding: 25px;
            border: 1px solid #e6edf5;
            border-radius: 20px;
            background: rgba(255, 255, 255, 0.95);
            box-shadow: 0 8px 22px rgba(34, 70, 110, 0.08);
            transition: 0.2s;
        }

        .info-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 26px rgba(34, 70, 110, 0.15);
        }

        .card-icon {
            font-size: 35px;
            margin-bottom: 8px;
        }

        .card-title {
            color: #164d87;
            font-size: 21px;
            font-weight: 800;
            margin-bottom: 8px;
        }

        .card-text {
            color: #455466;
            font-size: 16px;
            line-height: 1.75;
        }

        /* 교훈 */
        .motto-box {
            padding: 33px 20px;
            border-left: 8px solid #f2bd35;
            border-radius: 18px;
            text-align: center;
            color: #163d67;
            background: linear-gradient(135deg, #fff9e8, #ffffff);
            box-shadow: 0 7px 20px rgba(100, 80, 20, 0.08);
        }

        .motto-text {
            font-size: 28px;
            font-weight: 900;
            line-height: 1.7;
        }

        /* 연혁 */
        .timeline-item {
            padding: 14px 18px;
            margin: 10px 0;
            border-left: 5px solid #2878c8;
            border-radius: 0 14px 14px 0;
            background: white;
            box-shadow: 0 4px 13px rgba(40, 80, 120, 0.07);
        }

        .timeline-year {
            display: inline-block;
            min-width: 92px;
            color: #1762aa;
            font-weight: 900;
        }

        /* 퀴즈 결과 */
        .quiz-success {
            padding: 17px;
            border-radius: 14px;
            color: #12633b;
            background: #eafff2;
            border: 1px solid #bce9ce;
            font-weight: 700;
        }

        /* 하단 */
        .footer {
            margin-top: 45px;
            padding: 25px;
            border-radius: 18px;
            text-align: center;
            color: #657586;
            background: #eef5fb;
            line-height: 1.8;
        }

        /* Streamlit 버튼 */
        .stButton > button {
            border: none;
            border-radius: 12px;
            color: white;
            background: linear-gradient(90deg, #1764ad, #249568);
            font-weight: 800;
            padding: 10px 20px;
        }

        .stButton > button:hover {
            color: white;
            border: none;
            transform: translateY(-2px);
        }

        /* 모바일 화면 */
        @media (max-width: 700px) {
            .hero {
                padding: 38px 18px;
            }

            .hero h1 {
                font-size: 35px;
            }

            .hero p {
                font-size: 17px;
            }

            .motto-text {
                font-size: 22px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------
# 사이드바
# ---------------------------------------------------
with st.sidebar:
    st.title("🏫 방배중학교")

    menu = st.radio(
        "메뉴를 선택하세요.",
        [
            "학교 홈",
            "학교 소개",
            "학교 연혁",
            "학교 상징",
            "학교생활 퀴즈",
            "찾아오는 길",
        ],
    )

    st.divider()

    st.markdown(
        """
        ### 학교 기본 정보

        **학교 구분**  
        공립 중학교

        **개교**  
        1981년

        **관할 교육청**  
        서울특별시교육청

        **교육지원청**  
        강남서초교육지원청
        """
    )

    st.link_button(
        "🔗 공식 홈페이지",
        "https://bangbae.sen.ms.kr",
        use_container_width=True,
    )

    st.link_button(
        "🔍 학교알리미",
        "https://www.schoolinfo.go.kr",
        use_container_width=True,
    )


# ---------------------------------------------------
# 공통 제목
# ---------------------------------------------------
def section_title(icon, title, description):
    st.markdown(f"## {icon} {title}")
    st.caption(description)
    st.divider()


# ---------------------------------------------------
# 학교 홈
# ---------------------------------------------------
if menu == "학교 홈":
    st.markdown(
        """
        <div class="hero">
            <div class="hero-badge">BANGBAE MIDDLE SCHOOL</div>
            <h1>방배중학교</h1>
            <p>바른 마음 · 튼튼한 몸 · 부지런한 사람</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("## 방배중학교에 오신 것을 환영합니다")

    st.write(
        """
        방배중학교는 서울특별시 서초구에 위치한 공립 중학교입니다.
        학생들이 바른 인성과 건강한 몸을 기르고, 자신의 꿈을 향해
        부지런히 노력하도록 돕는 교육 공동체입니다.
        """
    )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="info-card">
                <div class="card-icon">💙</div>
                <div class="card-title">바른 마음</div>
                <div class="card-text">
                    다른 사람을 존중하고 배려하며
                    올바른 가치관을 지닌 사람으로 성장합니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="info-card">
                <div class="card-icon">💪</div>
                <div class="card-title">튼튼한 몸</div>
                <div class="card-text">
                    규칙적인 생활과 다양한 활동을 통해
                    건강한 몸과 강한 정신을 기릅니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="info-card">
                <div class="card-icon">📚</div>
                <div class="card-title">부지런한 사람</div>
                <div class="card-text">
                    스스로 목표를 세우고 꾸준히 공부하며
                    미래를 준비하는 사람으로 성장합니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.write("")

    st.markdown("## 학교 한눈에 보기")

    info1, info2, info3, info4 = st.columns(4)

    info1.metric("설립 인가", "1980년")
    info2.metric("첫 입학식", "1981년")
    info3.metric("설립 형태", "공립")
    info4.metric("학교 유형", "남녀공학")

    st.info(
        "이 사이트는 Streamlit을 이용해 만든 방배중학교 소개용 비공식 웹사이트입니다."
    )


# ---------------------------------------------------
# 학교 소개
# ---------------------------------------------------
elif menu == "학교 소개":
    section_title(
        "📖",
        "학교 소개",
        "방배중학교의 기본 정보와 교훈을 소개합니다.",
    )

    left, right = st.columns([1.3, 1])

    with left:
        st.markdown("### 학교 기본 정보")

        school_data = {
            "항목": [
                "학교명",
                "영문명",
                "설립 형태",
                "학교 유형",
                "설립 인가",
                "주소",
                "관할 기관",
            ],
            "내용": [
                "방배중학교",
                "Bangbae Middle School",
                "공립",
                "남녀공학 중학교",
                "1980년 12월 27일",
                "서울특별시 서초구 동광로 144",
                "서울특별시강남서초교육지원청",
            ],
        }

        st.table(school_data)

    with right:
        st.markdown("### 학교 교훈")

        st.markdown(
            """
            <div class="motto-box">
                <div class="motto-text">
                    바른 마음<br>
                    튼튼한 몸<br>
                    부지런한 사람
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.markdown("### 우리가 만들어 가는 학교")

    st.write(
        """
        방배중학교는 학생이 학교생활의 주인공이 되어 자신의 꿈과 재능을
        발견할 수 있도록 돕는 학교입니다. 교과 학습뿐 아니라 독서,
        예술, 체육, 진로 탐색과 학생자치활동 등을 통해 학생들이
        균형 있게 성장하는 것을 목표로 합니다.
        """
    )

    tab1, tab2, tab3 = st.tabs(
        ["🌱 인성", "🔎 배움", "🚀 미래"]
    )

    with tab1:
        st.subheader("존중과 배려")
        st.write(
            "친구와 선생님을 존중하고 서로 협력하는 학교 문화를 만들어 갑니다."
        )

    with tab2:
        st.subheader("스스로 배우는 힘")
        st.write(
            "질문하고 탐구하며 자신의 생각을 표현하는 학습 태도를 기릅니다."
        )

    with tab3:
        st.subheader("꿈을 향한 도전")
        st.write(
            "다양한 진로를 탐색하고 자신의 적성과 재능을 발견하도록 돕습니다."
        )


# ---------------------------------------------------
# 학교 연혁
# ---------------------------------------------------
elif menu == "학교 연혁":
    section_title(
        "🕰️",
        "학교 연혁",
        "방배중학교가 걸어온 주요 발자취입니다.",
    )

    history = [
        ("1980. 12. 27.", "방배중학교 설립 인가"),
        ("1981. 03. 01.", "초대 교장 취임"),
        ("1981. 03. 05.", "제1회 입학식 및 개학식"),
        ("1982. 02. 10.", "제1회 졸업식"),
        ("1984. 08. 27.", "현재의 학교 건물로 이전"),
        ("1984. 10. 26.", "남녀공학 시범학교 운영 발표"),
        ("2005. 05. 01.", "ICT 국제교류협력 연구학교 지정"),
        ("2013. 09. 05.", "아름다운 학교 만들기 교육감 표창"),
        ("2017. 12. 28.", "학생자치활동 활성화 우수학교 표창"),
    ]

    for date, event in history:
        st.markdown(
            f"""
            <div class="timeline-item">
                <span class="timeline-year">{date}</span>
                <span>{event}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.success(
        "방배중학교는 1981년 첫 입학식을 시작으로 오랜 전통을 이어오고 있습니다."
    )


# ---------------------------------------------------
# 학교 상징
# ---------------------------------------------------
elif menu == "학교 상징":
    section_title(
        "🌳",
        "학교 상징",
        "방배중학교를 나타내는 교목과 교화를 알아봅니다.",
    )

    tree_col, flower_col = st.columns(2)

    with tree_col:
        st.markdown(
            """
            <div class="info-card">
                <div class="card-icon">🌳</div>
                <div class="card-title">교목 · 은행나무</div>
                <div class="card-text">
                    은행나무는 오랜 세월을 견디며 크게 자라는 나무입니다.
                    굳건함과 끈기, 꾸준한 성장을 떠올리게 합니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with flower_col:
        st.markdown(
            """
            <div class="info-card">
                <div class="card-icon">🌼</div>
                <div class="card-title">교화 · 개나리</div>
                <div class="card-text">
                    개나리는 봄을 알리는 밝고 생기 넘치는 꽃입니다.
                    희망과 활기찬 학교생활을 떠올리게 합니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.write("")

    st.markdown("### 상징이 전하는 의미")

    symbol = st.selectbox(
        "궁금한 학교 상징을 선택하세요.",
        ["은행나무", "개나리", "학교 교훈"],
    )

    if symbol == "은행나무":
        st.info(
            "은행나무처럼 어려움에도 흔들리지 않고 꾸준히 성장하는 학생을 상징합니다."
        )

    elif symbol == "개나리":
        st.info(
            "개나리처럼 밝고 희망찬 마음으로 학교생활을 하는 학생을 상징합니다."
        )

    else:
        st.info(
            "바른 인성과 건강한 몸을 갖추고 성실하게 노력하는 사람으로 성장하자는 뜻입니다."
        )


# ---------------------------------------------------
# 퀴즈
# ---------------------------------------------------
elif menu == "학교생활 퀴즈":
    section_title(
        "🧩",
        "방배중학교 퀴즈",
        "학교 소개 내용을 얼마나 잘 기억하고 있는지 확인해 보세요.",
    )

    score = 0

    with st.form("school_quiz"):
        q1 = st.radio(
            "1. 방배중학교의 설립 형태는 무엇일까요?",
            ["사립", "공립", "국립"],
            index=None,
        )

        q2 = st.radio(
            "2. 방배중학교의 교목은 무엇일까요?",
            ["소나무", "은행나무", "단풍나무"],
            index=None,
        )

        q3 = st.radio(
            "3. 방배중학교의 교화는 무엇일까요?",
            ["장미", "무궁화", "개나리"],
            index=None,
        )

        q4 = st.radio(
            "4. 다음 중 학교 교훈에 포함된 것은 무엇일까요?",
            ["부지런한 사람", "유명한 사람", "완벽한 사람"],
            index=None,
        )

        submitted = st.form_submit_button(
            "정답 확인",
            use_container_width=True,
        )

    if submitted:
        if q1 == "공립":
            score += 1
        if q2 == "은행나무":
            score += 1
        if q3 == "개나리":
            score += 1
        if q4 == "부지런한 사람":
            score += 1

        st.markdown(f"## 퀴즈 결과: {score} / 4점")

        st.progress(score / 4)

        if score == 4:
            st.balloons()
            st.success("완벽합니다! 방배중학교에 대해 아주 잘 알고 있네요!")
        elif score >= 2:
            st.info("잘했습니다! 학교 소개를 한 번 더 보면 만점을 받을 수 있어요.")
        else:
            st.warning("학교 소개와 학교 상징 메뉴를 다시 살펴보세요.")

        with st.expander("정답 보기"):
            st.write("1번: 공립")
            st.write("2번: 은행나무")
            st.write("3번: 개나리")
            st.write("4번: 부지런한 사람")


# ---------------------------------------------------
# 찾아오는 길
# ---------------------------------------------------
elif menu == "찾아오는 길":
    section_title(
        "📍",
        "찾아오는 길",
        "방배중학교의 주소와 관련 정보를 확인할 수 있습니다.",
    )

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown("### 학교 주소")

        st.markdown(
            """
            <div class="info-card">
                <div class="card-icon">🏫</div>
                <div class="card-title">방배중학교</div>
                <div class="card-text">
                    서울특별시 서초구 동광로 144<br><br>
                    관할 교육지원청:<br>
                    서울특별시강남서초교육지원청
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown("### 관련 사이트")

        st.link_button(
            "🌐 방배중학교 공식 홈페이지",
            "https://bangbae.sen.ms.kr",
            use_container_width=True,
        )

        st.link_button(
            "🗺️ 네이버 지도에서 검색",
            "https://map.naver.com/p/search/방배중학교",
            use_container_width=True,
        )

        st.link_button(
            "🗺️ 카카오맵에서 검색",
            "https://map.kakao.com/?q=방배중학교",
            use_container_width=True,
        )

        st.link_button(
            "📊 학교알리미에서 검색",
            "https://www.schoolinfo.go.kr",
            use_container_width=True,
        )

    st.warning(
        "방문 전에는 학교 공식 홈페이지에서 정확한 연락처와 방문 안내를 확인하세요."
    )


# ---------------------------------------------------
# 하단 안내
# ---------------------------------------------------
st.markdown(
    """
    <div class="footer">
        <strong>방배중학교 소개 웹사이트</strong><br>
        이 사이트는 학생이 Streamlit 학습 목적으로 제작한 비공식 소개 사이트입니다.<br>
        정확한 최신 정보는 방배중학교 공식 홈페이지와 학교알리미를 확인해 주세요.
    </div>
    """,
    unsafe_allow_html=True,
)
