import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import os

st.title("📂 CSV 파일 업로드 및 데이터 시각화")

# NanumGothic 폰트 파일 경로 (프로젝트 루트 기준)
font_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../fonts/NanumGothic-Regular.ttf"))

# 폰트 파일이 존재할 때만 폰트 설정
if os.path.exists(font_path):
    fontprop = font_manager.FontProperties(fname=font_path)
    plt.rcParams['font.family'] = fontprop.get_name()
    plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지
else:
    st.warning("한글 폰트 파일을 찾을 수 없습니다. 한글이 깨질 수 있습니다.")
    fontprop = None

# 파일 업로드 위젯
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # CSV 파일을 데이터프레임으로 읽기
    df = pd.read_csv(uploaded_file)
    st.subheader("데이터 미리보기")
    st.dataframe(df)  # 데이터프레임 표시

    # 컬럼 선택 (수치형 컬럼만)
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    if len(numeric_cols) >= 1:
        st.subheader("컬럼별 데이터 시각화")
        col = st.selectbox("시각화할 수치형 컬럼을 선택하세요", numeric_cols)
        # 히스토그램 그리기
        fig, ax = plt.subplots()
        ax.hist(df[col].dropna(), bins=20, color='skyblue', edgecolor='black')
        # 폰트가 있으면 fontproperties 적용, 없으면 기본 폰트 사용
        if fontprop:
            ax.set_title(f"'{col}' 컬럼의 분포", fontproperties=fontprop)
            ax.set_xlabel(col, fontproperties=fontprop)
            ax.set_ylabel("빈도수", fontproperties=fontprop)
        else:
            ax.set_title(f"'{col}' 컬럼의 분포")
            ax.set_xlabel(col)
            ax.set_ylabel("빈도수")
        st.pyplot(fig)
    else:
        st.info("시각화할 수치형 컬럼이 없습니다.")
else:
    st.info("CSV 파일을 업로드하면 데이터와 시각화 결과가 표시됩니다.")

# 각 단계별로 코드에 주석을 달았습니다.