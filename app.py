import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="CSV Data Analyzer", layout="wide")

st.title("📊 CSV 데이터 자동 분석 앱")
st.write("CSV 파일을 업로드하면 기본 통계 요약, 컬럼별 그래프를 자동으로 생성해줍니다.")

uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # Load CSV
    df = pd.read_csv(uploaded_file)

    st.subheader("📌 데이터 미리보기")
    st.dataframe(df.head())

    st.subheader("📌 기본 정보")
    st.write(f"- 행(row) 수: **{df.shape[0]}**")
    st.write(f"- 열(column) 수: **{df.shape[1]}**")

    st.subheader("📌 통계 요약 (describe())")
    st.dataframe(df.describe(include="all"))

    st.subheader("📊 컬럼별 그래프 자동 생성")

    numeric_cols = df.select_dtypes(include=["int", "float"]).columns

    if len(numeric_cols) > 0:
        selected_col = st.selectbox("그래프를 볼 숫자형 컬럼 선택", numeric_cols)

        fig, ax = plt.subplots()
        ax.hist(df[selected_col].dropna(), bins=20)
        ax.set_title(f"Histogram of {selected_col}")
        ax.set_xlabel(selected_col)
        ax.set_ylabel("Frequency")

        st.pyplot(fig)
    else:
        st.write("숫자형 컬럼이 없어 그래프를 생성할 수 없습니다.")

else:
    st.info("CSV 파일을 업로드하면 분석 결과가 여기에 표시됩니다.")
