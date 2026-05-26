# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="Countries MBTI Dashboard",
    layout="centered"
)

st.title("🌍 Countries MBTI Dashboard")
st.write("국가를 선택하면 MBTI 비율을 시각화합니다.")

# -----------------------------
# 데이터 불러오기
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# -----------------------------
# 국가 선택
# -----------------------------
countries = sorted(df["Country"].unique())

selected_country = st.selectbox(
    "국가 선택",
    countries
)

# -----------------------------
# 선택 국가 데이터
# -----------------------------
country_data = df[df["Country"] == selected_country].iloc[0]

mbti_columns = [col for col in df.columns if col != "Country"]

values = country_data[mbti_columns].astype(float)

# 내림차순 정렬
sorted_values = values.sort_values(ascending=False)

# -----------------------------
# 색상 설정
# 1등 = 노란색
# 나머지 = 하늘색 그라데이션
# -----------------------------
top_color = "#FFD700"  # gold

base_blue = np.array(mcolors.to_rgb("#87CEEB"))  # skyblue
white = np.array([1, 1, 1])

colors = [top_color]

n = len(sorted_values) - 1

for i in range(n):
    ratio = i / max(n - 1, 1)

    # skyblue -> white
    color = base_blue * (1 - ratio) + white * ratio
    colors.append(color)

# -----------------------------
# 그래프 생성
# -----------------------------
fig, ax = plt.subplots(figsize=(12, 6))

bars = ax.bar(
    sorted_values.index,
    sorted_values.values,
    color=colors
)

# 값 표시
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.002,
        f"{height:.2%}",
        ha='center',
        fontsize=9
    )

ax.set_title(f"{selected_country} MBTI Distribution", fontsize=16)
ax.set_ylabel("Percentage")
ax.set_ylim(0, sorted_values.max() * 1.15)

plt.xticks(rotation=45)

st.pyplot(fig)

# -----------------------------
# 데이터 테이블
# -----------------------------
st.subheader("📊 상세 데이터")

display_df = pd.DataFrame({
    "MBTI": sorted_values.index,
    "Ratio": sorted_values.values
})

display_df["Ratio"] = (display_df["Ratio"] * 100).round(2).astype(str) + "%"

st.dataframe(display_df, use_container_width=True)
