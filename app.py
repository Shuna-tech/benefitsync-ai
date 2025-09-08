import streamlit as st
import pandas as pd

# 示例：替换为你自己的分析逻辑
def analyze_feedback(df):
    df['Sentiment'] = df['Comment'].apply(lambda x: 'Positive' if 'good' in str(x).lower() else 'Negative')
    df['Category'] = 'Coverage Issues'  # 你可以用 OpenAI/LangChain 分类
    df['Route To'] = 'Benefits Admin'
    df['Severity'] = 3
    return df

st.title("🧠 BenefitsSync AI — Phase 1: Feedback Analyzer")

uploaded_file = st.file_uploader("Upload your feedback_data.csv", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Raw Data")
    st.dataframe(df)

    if st.button("Analyze"):
        analyzed_df = analyze_feedback(df)
        st.subheader("📊 Analysis Results")
        st.dataframe(analyzed_df)
        st.download_button("⬇️ Download CSV", analyzed_df.to_csv(index=False), "analyzed_feedback.csv")
