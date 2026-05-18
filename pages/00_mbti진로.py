```python
import streamlit as st

st.set_page_config(
    page_title="✨ MBTI 진로 추천기",
    page_icon="🚀",
    layout="centered"
)

# -----------------------------
# MBTI별 진로 데이터
# -----------------------------
career_data = {
    "INTJ": [
        {
            "job": "🧠 데이터 사이언티스트",
            "major": "컴퓨터공학과, 통계학과",
            "personality": "분석적이고 전략 세우는 걸 좋아하는 사람!",
            "salary": "평균 연봉 약 5,500만 원"
        },
        {
            "job": "🏗️ 건축가",
            "major": "건축학과",
            "personality": "창의적이면서 계획적인 성격에 딱!",
            "salary": "평균 연봉 약 5,000만 원"
        }
    ],

    "INTP": [
        {
            "job": "💻 프로그래머",
            "major": "소프트웨어학과, 컴퓨터공학과",
            "personality": "호기심 많고 문제 해결 좋아하는 타입!",
            "salary": "평균 연봉 약 5,200만 원"
        },
        {
            "job": "🔬 연구원",
            "major": "물리학과, 화학과",
            "personality": "깊게 탐구하는 걸 좋아하면 추천!",
            "salary": "평균 연봉 약 4,800만 원"
        }
    ],

    "ENTJ": [
        {
            "job": "📈 경영 컨설턴트",
            "major": "경영학과",
            "personality": "리더십 있고 추진력 강한 사람!",
            "salary": "평균 연봉 약 6,000만 원"
        },
        {
            "job": "🚀 스타트업 CEO",
            "major": "경영학과, 경제학과",
            "personality": "도전 정신 넘치는 성격과 찰떡!",
            "salary": "평균 연봉 약 7,000만 원 이상"
        }
    ],

    "ENTP": [
        {
            "job": "🎤 마케팅 기획자",
            "major": "광고홍보학과",
            "personality": "아이디어 넘치고 말 잘하는 타입!",
            "salary": "평균 연봉 약 4,500만 원"
        },
        {
            "job": "📺 콘텐츠 크리에이터",
            "major": "미디어학과",
            "personality": "창의력 폭발하는 사람에게 추천!",
            "salary": "평균 연봉 약 4,000만 원 이상"
        }
    ],

    "INFJ": [
        {
            "job": "💖 심리상담사",
            "major": "심리학과",
            "personality": "공감 능력 뛰어난 사람!",
            "salary": "평균 연봉 약 4,200만 원"
        },
        {
            "job": "📚 작가",
            "major": "문예창작학과",
            "personality": "상상력 풍부하고 감성적인 타입!",
            "salary": "평균 연봉 약 3,800만 원"
        }
    ],

    "INFP": [
        {
            "job": "🎨 일러스트레이터",
            "major": "디자인학과",
            "personality": "감성적이고 창의적인 사람!",
            "salary": "평균 연봉 약 3,500만 원"
        },
        {
            "job": "🎵 음악 프로듀서",
            "major": "실용음악과",
            "personality": "자기만의 감성을 표현하는 걸 좋아한다면 추천!",
            "salary": "평균 연봉 약 4,000만 원"
        }
    ],

    "ENFJ": [
        {
            "job": "👩‍🏫 교사",
            "major": "교육학과",
            "personality": "사람 챙기는 걸 좋아하는 따뜻한 성격!",
            "salary": "평균 연봉 약 5,000만 원"
        },
        {
            "job": "🤝 HR 매니저",
            "major": "경영학과",
            "personality": "사람과 협업 잘하는 타입!",
            "salary": "평균 연봉 약 5,500만 원"
        }
    ],

    "ENFP": [
        {
            "job": "🎬 방송 PD",
            "major": "미디어학과",
            "personality": "열정 넘치고 아이디어 많은 성격!",
            "salary": "평균 연봉 약 5,000만 원"
        },
        {
            "job": "✈️ 여행 콘텐츠 기획자",
            "major": "관광경영학과",
            "personality": "새로운 경험 좋아하면 완전 추천!",
            "salary": "평균 연봉 약 4,200만 원"
        }
    ],

    "ISTJ": [
        {
            "job": "🏦 회계사",
            "major": "회계학과",
            "personality": "꼼꼼하고 책임감 강한 사람!",
            "salary": "평균 연봉 약 6,000만 원"
        },
        {
            "job": "⚖️ 공무원",
            "major": "행정학과",
            "personality": "안정적이고 체계적인 걸 좋아한다면 추천!",
            "salary": "평균 연봉 약 4,500만 원"
        }
    ],

    "ISFJ": [
        {
            "job": "🏥 간호사",
            "major": "간호학과",
            "personality": "배려심 많고 책임감 있는 성격!",
            "salary": "평균 연봉 약 4,800만 원"
        },
        {
            "job": "👶 유치원 교사",
            "major": "유아교육과",
            "personality": "아이들을 좋아하는 따뜻한 타입!",
            "salary": "평균 연봉 약 3,800만 원"
        }
    ],

    "ESTJ": [
        {
            "job": "🏢 기업 관리자",
            "major": "경영학과",
            "personality": "리더십 있고 조직 관리 잘하는 사람!",
            "salary": "평균 연봉 약 5,800만 원"
        },
        {
            "job": "👮 경찰관",
            "major": "경찰행정학과",
            "personality": "책임감 강하고 정의로운 타입!",
            "salary": "평균 연봉 약 4,700만 원"
        }
    ],

    "ESFJ": [
        {
            "job": "💄 서비스 매니저",
            "major": "호텔관광학과",
            "personality": "친절하고 사람 만나는 걸 좋아하는 성격!",
            "salary": "평균 연봉 약 4,200만 원"
        },
        {
            "job": "🎉 이벤트 플래너",
            "major": "이벤트학과",
            "personality": "분위기 메이커라면 추천!",
            "salary": "평균 연봉 약 4,000만 원"
        }
    ],

    "ISTP": [
        {
            "job": "🔧 기계 엔지니어",
            "major": "기계공학과",
            "personality": "손으로 직접 만드는 걸 좋아하는 타입!",
            "salary": "평균 연봉 약 5,500만 원"
        },
        {
            "job": "🛩️ 파일럿",
            "major": "항공운항학과",
            "personality": "침착하고 현실적인 성격에 잘 맞음!",
            "salary": "평균 연봉 약 7,000만 원"
        }
    ],

    "ISFP": [
        {
            "job": "📷 사진작가",
            "major": "사진학과",
            "personality": "감각적이고 자유로운 영혼!",
            "salary": "평균 연봉 약 3,500만 원"
        },
        {
            "job": "🎀 패션 디자이너",
            "major": "패션디자인학과",
            "personality": "예술 감각 뛰어난 사람 추천!",
            "salary": "평균 연봉 약 4,200만 원"
        }
    ],

    "ESTP": [
        {
            "job": "💼 영업 전문가",
            "major": "경영학과",
            "personality": "사교성 좋고 에너지 넘치는 타입!",
            "salary": "평균 연봉 약 5,000만 원"
        },
        {
            "job": "🏀 스포츠 매니저",
            "major": "스포츠산업학과",
            "personality": "활동적이고 도전 좋아하는 사람!",
            "salary": "평균 연봉 약 4,500만 원"
        }
    ],

    "ESFP": [
        {
            "job": "🎤 연예인/방송인",
            "major": "연극영화과",
            "personality": "끼 많고 사람들과 어울리기 좋아하는 타입!",
            "salary": "평균 연봉 약 5,000만 원 이상"
        },
        {
            "job": "🍰 파티시에",
            "major": "제과제빵학과",
            "personality": "손재주 좋고 감각적인 성격!",
            "salary": "평균 연봉 약 3,800만 원"
        }
    ]
}

# -----------------------------
# 제목
# -----------------------------
st.title("✨ MBTI 진로 추천기 🚀")
st.write("나의 MBTI에 맞는 진로를 알아보자! 😎")

# -----------------------------
# MBTI 선택
# -----------------------------
mbti = st.selectbox(
    "🧩 너의 MBTI를 골라줘!",
    list(career_data.keys())
)

# -----------------------------
# 결과 출력
# -----------------------------
if st.button("🔍 진로 추천 받기"):
    st.subheader(f"🎉 {mbti} 유형 추천 진로!")

    careers = career_data[mbti]

    for idx, career in enumerate(careers, start=1):
        st.markdown(f"""
        ---
        ## {idx}. {career['job']}

        ### 📚 추천 학과
        👉 {career['major']}

        ### 😆 잘 맞는 성격
        👉 {career['personality']}

        ### 💰 평균 연봉
        👉 {career['salary']}
        """)

    st.success("✨ 미래는 아직 무한 가능성! 재미있게 참고해봐 😄")
```
