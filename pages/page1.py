import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# NanumGothic 폰트 파일 경로 지정
font_path = "./fonts/NanumGothic-Regular.ttf"  # pages/ 기준 상대경로

# 폰트 등록 및 설정
fontprop = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = fontprop.get_name()
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

st.title("📊 Matplotlib 데이터 시각화 예시")

st.write("아래는 Matplotlib을 활용한 간단한 데이터 시각화 예시입니다. 그래프의 제목과 축 레이블에 한글이 정상적으로 표시됩니다.")

# 예시 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y, label='사인 곡선')
ax.set_title('사인 함수 그래프', fontproperties=fontprop)
ax.set_xlabel('x 값', fontproperties=fontprop)
ax.set_ylabel('y 값', fontproperties=fontprop)
ax.legend(prop=fontprop)

# Streamlit에 그래프 출력
st.pyplot(fig)

# 각 단계별로 코드에 대한 설명을 추가했습니다.