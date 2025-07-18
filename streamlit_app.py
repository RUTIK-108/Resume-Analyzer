import streamlit as st
from resume_parser import get_resume_text
from jd_processing import clean_text
from utils import compute_similarity, detect_skills

st.set_page_config(page_title="Resume Analyzer", layout="wide")

st.title("📄 Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF/DOCX)", type=['pdf', 'docx'])
jd_input = st.text_area("Paste the Job Description here")

if uploaded_file and jd_input:
    with st.spinner("Analyzing..."):
        resume_text = get_resume_text(uploaded_file)
        jd_clean = clean_text(jd_input)
        resume_clean = clean_text(resume_text)

        score = compute_similarity(resume_clean, jd_clean)

        with open("skills.txt") as f:
            skill_list = [line.strip() for line in f.readlines()]

        detected = detect_skills(resume_text, skill_list)

        st.subheader("🔍 Match Score")
        st.progress(int(score))
        st.write(f"**Match Score:** {score}%")

        st.subheader("🧠 Detected Skills")
        st.write(", ".join(detected))

        st.subheader("📌 Suggestions")
        missing = [skill for skill in skill_list if skill not in detected and skill in jd_input]
        if missing:
            st.warning(f"Consider adding these skills: {', '.join(missing)}")
        else:
            st.success("All relevant skills matched!")
