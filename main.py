import streamlit as st

# 🎨 앱 기본 설정
st.set_page_config(page_title="MBTI 직업 추천", page_icon="🧠")

# 🌟 제목
st.title("MBTI 직업 추천 앱 💼")
st.subheader("당신의 MBTI에 어울리는 직업은? 😄")

# 🔍 MBTI 목록
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 🎯 직업 추천 딕셔너리
mbti_jobs = {
    "INTJ": ["데이터 과학자 🧪", "전략 컨설턴트 📊", "소프트웨어 아키텍트 💻"],
    "INTP": ["연구원 🔬", "이론 물리학자 🧠", "기술 분석가 🧯"],
    "ENTJ": ["CEO 👩‍💼", "프로젝트 매니저 📈", "변호사 ⚖️"],
    "ENTP": ["기업가 🚀", "마케팅 디렉터 📣", "정치 전략가 🗳️"],
    "INFJ": ["상담가 🧘‍♂️", "작가 ✍️", "교육자 👩‍🏫"],
    "INFP": ["시인 📜", "예술가 🎨", "사회복지사 🤝"],
    "ENFJ": ["리더십 코치 🗣️", "HR 매니저 🧑‍💼", "사회운동가 ✊"],
    "ENFP": ["방송인 🎤", "크리에이터 📸", "이벤트 플래너 🎉"],
    "ISTJ": ["회계사 🧾", "공무원 🏢", "보안 전문가 🔐"],
    "ISFJ": ["간호사 👩‍⚕️", "초등교사 🏫", "도서관 사서 📚"],
    "ESTJ": ["군인 🪖", "경영 관리자 🧑‍💼", "프로젝트 관리자 🛠️"],
    "ESFJ": ["고객 서비스 담당자 ☎️", "간호조무사 👩‍⚕️", "교사 🍎"],
    "ISTP": ["기술자 🔧", "파일럿 ✈️", "자동차 정비사 🚗"],
    "ISFP": ["패션 디자이너 👗", "사진작가 📷", "요리사 🍳"],
    "ESTP": ["영업 전문가 💼", "소방관 🚒", "스턴트맨 🎬"],
    "ESFP": ["연예인 🌟", "이벤트 진행자 🎙️", "뷰티 유튜버 💄"]
}

# 🧩 사용자 입력
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요 👇", mbti_types)

# 🚀 결과 출력
if selected_mbti:
    st.markdown(f"### 🧠 {selected_mbti}에게 추천하는 직업들:")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")

# 🎉 푸터
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
