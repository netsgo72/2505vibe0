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

# 🎯 MBTI별 직업과 설명
mbti_recommendations = {
    "INTJ": [
        ("데이터 과학자 🧪", "논리적 사고와 독립적인 분석 능력이 뛰어나 복잡한 데이터를 다루기에 적합합니다."),
        ("전략 컨설턴트 📊", "전체를 보는 통찰력과 계획 수립 능력으로 기업 전략을 설계하는 데 강점을 보입니다."),
        ("소프트웨어 아키텍트 💻", "구조적 사고와 시스템적인 접근으로 기술 설계를 잘 수행할 수 있습니다.")
    ],
    "INFP": [
        ("시인 📜", "깊은 감성과 상상력으로 감정을 언어로 아름답게 표현하는 데 탁월합니다."),
        ("예술가 🎨", "창의력과 내면의 세계를 표현하는 데 열정적이며 섬세한 감각이 뛰어납니다."),
        ("사회복지사 🤝", "타인의 감정을 잘 이해하고 공감하는 능력으로 도움을 주는 일을 잘 수행합니다.")
    ],
    "ENTP": [
        ("기업가 🚀", "새로운 아이디어와 도전을 즐기며 기회를 포착하고 추진하는 데 강한 열정을 가집니다."),
        ("마케팅 디렉터 📣", "창의적인 기획과 대중과의 소통 능력으로 브랜드 가치를 높일 수 있습니다."),
        ("정치 전략가 🗳️", "빠른 사고력과 설득력으로 사람들을 이끌고 복잡한 상황을 전략적으로 풀 수 있습니다.")
    ],
    "ISFJ": [
        ("간호사 👩‍⚕️", "헌신적이고 세심한 성격으로 환자의 요구를 따뜻하게 돌볼 수 있습니다."),
        ("초등교사 🏫", "아이들의 성장에 관심이 많고 인내심이 많아 교육 분야에 잘 맞습니다."),
        ("도서관 사서 📚", "조용하고 체계적인 환경에서 정보 정리와 관리 능력을 발휘할 수 있습니다.")
    ],
    # 원하는 만큼 추가 가능
}

# 🧩 사용자 입력
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요 👇", mbti_types)

# 🚀 결과 출력
if selected_mbti:
    st.markdown(f"### 🧠 {selected_mbti}에게 추천하는 직업들:")
    if selected_mbti in mbti_recommendations:
        for job, reason in mbti_recommendations[selected_mbti]:
            st.markdown(f"- **{job}**  \n  👉 {reason}")
    else:
        st.warning("아직 이 MBTI에 대한 추천 정보가 준비되지 않았어요. 😢")

# 🎉 푸터
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
