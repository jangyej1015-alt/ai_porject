# app.py

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="서울 인구 연령별 분석",
    layout="wide"
)

st.title("📊 서울시 행정구별 연령 인구 분석")
st.markdown("행정구를 선택하면 연령별 인구 분포를 확인할 수 있습니다.")

# -----------------------------
# 한글 폰트 설정
# -----------------------------
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# -----------------------------
# 데이터 불러오기
# -----------------------------
@st.cache_data

def load_data():
    df = pd.read_csv('population.csv', encoding='utf-8')
    return df


df = load_data()

# -----------------------------
# 행정구 선택
# -----------------------------
region_col = df.columns[0]
regions = df[region_col].tolist()

selected_region = st.selectbox(
    '행정구를 선택하세요',
    regions
)

# -----------------------------
# 선택된 행정구 데이터 추출
# -----------------------------
selected_df = df[df[region_col] == selected_region]

# 2026년04월 기준 연령 컬럼 추출
age_columns = [
    col for col in df.columns
    if '2026년04월_거주자_' in col
    and '세' in col
    and '총인구수' not in col
]

ages = []
populations = []

for col in age_columns:
    try:
        age_text = col.split('_')[-1].replace('세', '')

        if '이상' in age_text:
            age = 100
        else:
            age = int(age_text)

        population = int(selected_df[col].values[0].replace(',', ''))

        ages.append(age)
        populations.append(population)

    except:
        pass

# -----------------------------
# 데이터프레임 생성
# -----------------------------
plot_df = pd.DataFrame({
    '나이': ages,
    '인구수': populations
}).sort_values('나이')

# -----------------------------
# 그래프 그리기
# -----------------------------
fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(
    plot_df['나이'],
    plot_df['인구수'],
    color='hotpink',
    linewidth=3
)

# 제목
ax.set_title(
    f'{selected_region} 연령별 인구 분포',
    fontsize=18,
    fontweight='bold'
)

# 축 라벨
ax.set_xlabel('나이', fontsize=14)
ax.set_ylabel('인구수', fontsize=14)

# x축 10살 단위 구분선
ax.set_xticks(range(0, 101, 10))
ax.grid(True, axis='x', linestyle='--', alpha=0.7)

# y축 숫자 포맷
ax.ticklabel_format(style='plain', axis='y')

st.pyplot(fig)

# -----------------------------
# 데이터 표 보기
# -----------------------------
st.subheader('📋 연령별 인구 데이터')
st.dataframe(plot_df, use_container_width=True)
```

---

# requirements.txt

```txt
streamlit
pandas
matplotlib
```

---

# Streamlit Cloud 배포 방법

## 1. 깃허브 업로드

다음 파일들을 GitHub 저장소에 업로드하세요.

* app.py
* population.csv
* requirements.txt

---

## 2. Streamlit Cloud 접속

urlStreamlit Cloud[https://streamlit.io/cloud](https://streamlit.io/cloud)

---

## 3. 배포하기

1. "New app" 클릭
2. GitHub 저장소 선택
3. app.py 선택
4. Deploy 클릭

---

## 4. 실행 결과

기능:

* 행정구 선택
* 연령별 인구 꺾은선 그래프
* 핫핑크 색상 적용
* 10살 단위 세로 구분선
* 한글 폰트 깨짐 방지
* 데이터 테이블 표시
