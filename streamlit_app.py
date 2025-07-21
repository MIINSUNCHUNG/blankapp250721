import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

# 제목과 부제목
st.title("🎈 Streamlit 요소 예시 페이지")  # 페이지의 메인 타이틀
st.header("헤더 예시")                   # 큰 제목
st.subheader("서브헤더 예시")            # 작은 제목
st.text("이것은 일반 텍스트입니다.")      # 일반 텍스트

# 마크다운
st.markdown("**마크다운** _스타일링_도 지원합니다!")  # 마크다운 문법 사용

# 코드 블록
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')  # 코드 블록 표시

# 데이터프레임
import pandas as pd
df = pd.DataFrame({
    '이름': ['홍길동', '김철수', '이영희'],
    '나이': [28, 34, 22]
})
st.dataframe(df)  # 데이터프레임 테이블 표시

# 차트
import numpy as np
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)  # 선 그래프

# 이미지
st.image("https://static.streamlit.io/examples/cat.jpg", caption="고양이 이미지")  # 이미지 표시

# 오디오
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")  # 오디오 재생

# 비디오
st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # 비디오 재생

# 입력 위젯
name = st.text_input("이름을 입력하세요")  # 텍스트 입력
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120)  # 숫자 입력
agree = st.checkbox("동의하십니까?")  # 체크박스

# 버튼
if st.button("인사하기"):
    st.write(f"안녕하세요, {name}님!")  # 버튼 클릭 시 메시지 출력

# 슬라이더
value = st.slider("값을 선택하세요", 0, 100, 50)  # 슬라이더

# 셀렉트박스
color = st.selectbox("좋아하는 색을 선택하세요", ["빨강", "초록", "파랑"])  # 드롭다운

# 파일 업로드
uploaded_file = st.file_uploader("파일을 업로드하세요")  # 파일 업로드 위젯
if uploaded_file is not None:
    st.write("업로드된 파일 이름:", uploaded_file.name)

# 경고, 에러, 성공 메시지
st.success("성공 메시지 예시입니다!")  # 성공 메시지
st.warning("경고 메시지 예시입니다!")  # 경고 메시지
st.error("에러 메시지 예시입니다!")    # 에러 메시지

# 진행 바
import time
st.write("진행 바 예시:")
progress_bar = st.progress(0)
for percent_complete in range(0, 101, 10):
    time.sleep(0.05)
    progress_bar.progress(percent_complete)

# 사이드바
st.sidebar.title("사이드바 예시")  # 사이드바에 타이틀 추가
st.sidebar.button("사이드바 버튼")  # 사이드바에 버튼 추가

# 각주는 코드 내 주석(#)으로 설명을 달았습니다.
# 파이썬 리스트를 다루는 예제 페이지
st.title("📝 파이썬 리스트 실습 페이지")

st.write(
    """
    이 페이지에서는 파이썬의 리스트(list) 자료형에 대해 실습해볼 수 있습니다.
    아래에서 리스트에 값을 추가, 제거, 정렬하는 기능을 직접 사용해보세요!
    """
)

# 세션 상태를 사용하여 리스트를 저장
if "my_list" not in st.session_state:
    st.session_state.my_list = []

# 리스트 추가
st.subheader("1. 리스트에 값 추가하기")
new_item = st.text_input("추가할 값을 입력하세요")
if st.button("추가"):
    if new_item:
        st.session_state.my_list.append(new_item)  # 리스트에 값 추가
        st.success(f"'{new_item}'이(가) 리스트에 추가되었습니다.")

# 리스트 제거
st.subheader("2. 리스트에서 값 제거하기")
if st.session_state.my_list:
    remove_item = st.selectbox("제거할 값을 선택하세요", st.session_state.my_list)
    if st.button("제거"):
        st.session_state.my_list.remove(remove_item)  # 리스트에서 값 제거
        st.warning(f"'{remove_item}'이(가) 리스트에서 제거되었습니다.")
else:
    st.info("리스트에 값이 없습니다. 먼저 값을 추가해보세요.")

# 리스트 정렬
st.subheader("3. 리스트 정렬하기")
sort_order = st.radio("정렬 순서 선택", ("오름차순", "내림차순"))
if st.button("정렬"):
    st.session_state.my_list.sort(reverse=(sort_order == "내림차순"))  # 리스트 정렬
    st.success(f"리스트가 {sort_order}으로 정렬되었습니다.")

# 현재 리스트 출력
st.subheader("4. 현재 리스트 상태")
st.write(st.session_state.my_list)  # 리스트 출력

# 각 단계별로 코드 내 주석(#)으로 설명을 달았습니다.