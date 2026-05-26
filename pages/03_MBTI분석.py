# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# --------------------------------------------------
# 페이지 설정
# --------------------------------------------------
st.set_page_config(
    page_title="Countries MBTI Dashboard",
    layout="wide"
)

st.title("🌍 Countries MBTI Dashboard")
st.write("국가별 MBTI 비율과 MBTI별 상위 국가 랭킹을 확인하세요.")

# --------------------------------------------------
# 데이터 불러오기
# --------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# MBTI 컬럼
mbti_columns = [col for col in df.columns if col != "Country"]

# --------------------------------------------------
# 탭 구성
# --------------------------------------------------
tab1, tab2 = st.tabs([
    "📊 국가별 MBTI 비율",
    "🏆 MBTI별 TOP 10 국가"
])

# ==================================================
# TAB 1
# 국가 선택 -> MBTI 비율 그래프
# ==================================================
with tab1:

    st.header("국가별 MBTI 분포")

    countries = sorted(df["Country"].unique())

    selected_country = st.selectbox(
        "국가 선택",
        countries
    )

    # 선택 국가 데이터
    country_data = df[df["Country"] == selected_country].iloc[0]

    values = country_data[mbti_columns].astype(float)

    # 내림차순 정렬
    sorted_values = values.sort_values(ascending=False)

    # --------------------------------------------------
    # 색상 설정
    # 1등 = 노란색
    # 나머지 = 초록 그라데이션
    # --------------------------------------------------
    top_color = "#FFD700"

    base_green = np.array(mcolors.to_rgb("#2ecc71"))
    white = np.array([1, 1, 1])

    colors = [top_color]

    n = len(sorted_values) - 1

    for i in range(n):
        ratio = i / max(n - 1, 1)

        # 초록 -> 흰색
        color = base_green * (1 - ratio) + white * ratio
        colors.append(color)

    # --------------------------------------------------
    # 그래프
    # --------------------------------------------------
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

    ax.set_title(
        f"{selected_country} MBTI Distribution",
        fontsize=16
    )

    ax.set_ylabel("Percentage")
    ax.set_ylim(0, sorted_values.max() * 1.15)

    plt.xticks(rotation=45)

    st.pyplot(fig)

    # 상세 데이터
    st.subheader("📋 상세 데이터")

    display_df = pd.DataFrame({
        "MBTI": sorted_values.index,
        "Ratio": sorted_values.values
    })

    display_df["Ratio"] = (
        display_df["Ratio"] * 100
    ).round(2).astype(str) + "%"

    st.dataframe(
        display_df,
        use_container_width=True
    )

# ==================================================
# TAB 2
# MBTI 선택 -> 상위 10개 국가
# ==================================================
with tab2:

    st.header("MBTI별 상위 국가 TOP 10")

    selected_mbti = st.selectbox(
        "MBTI 선택",
        sorted(mbti_columns)
    )

    # 해당 MBTI 기준 정렬
    top10 = (
        df[["Country", selected_mbti]]
        .sort_values(by=selected_mbti, ascending=False)
        .head(10)
    )

    # --------------------------------------------------
    # 색상 설정
    # 1등 = 노란색
    # 나머지 = 초록 그라데이션
    # --------------------------------------------------
    top_color = "#FFD700"

    base_green = np.array(mcolors.to_rgb("#2ecc71"))
    white = np.array([1, 1, 1])

    colors = [top_color]

    n = len(top10) - 1

    for i in range(n):
        ratio = i / max(n - 1, 1)

        color = base_green * (1 - ratio) + white * ratio
        colors.append(color)

    # --------------------------------------------------
    # 그래프
    # --------------------------------------------------
    fig2, ax2 = plt.subplots(figsize=(12, 6))

    bars2 = ax2.bar(
        top10["Country"],
        top10[selected_mbti],
        color=colors
    )

    # 값 표시
    for idx, bar in enumerate(bars2):

        height = bar.get_height()

        ax2.text(
            bar.get_x() + bar.get_width()/2,
            height + 0.002,
            f"{height:.2%}",
            ha='center',
            fontsize=9
        )

    ax2.set_title(
        f"Top 10 Countries for {selected_mbti}",
        fontsize=16
    )

    ax2.set_ylabel("Percentage")

    plt.xticks(rotation=45)

    st.pyplot(fig2)

    # --------------------------------------------------
    # 순위 테이블
    # --------------------------------------------------
    st.subheader("🏅 랭킹")

    ranking_df = top10.copy()

    ranking_df.insert(0, "Rank", range(1, 11))

    ranking_df[selected_mbti] = (
        ranking_df[selected_mbti] * 100
    ).round(2).astype(str) + "%"

    ranking_df.columns = [
        "Rank",
        "Country",
        "Ratio"
    ]

    st.dataframe(
        ranking_df,
        use_container_width=True
    )
