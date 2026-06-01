import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(
    page_title="연도별 기온 비교",
    layout="wide"
)

st.title("🌡️ 서울 연도별 기온 비교")

# 현재 파일 위치 기준으로 상위 폴더의 seoul.csv 읽기
BASE_DIR = Path(__file__).resolve().parent.parent
csv_path = BASE_DIR / "seoul.csv"

try:
    df = pd.read_csv(csv_path, encoding="cp949")
except:
    df = pd.read_csv(csv_path, encoding="utf-8")

# 날짜 변환
df["날짜"] = pd.to_datetime(df["날짜"])

# 연도, 월, 일 생성
df["연도"] = df["날짜"].dt.year
df["월"] = df["날짜"].dt.month
df["일"] = df["날짜"].dt.day

col1, col2 = st.columns(2)

with col1:
    month = st.selectbox(
        "월 선택",
        sorted(df["월"].unique())
    )

with col2:
    available_days = sorted(
        df[df["월"] == month]["일"].unique()
    )

    day = st.selectbox(
        "일 선택",
        available_days
    )

# 선택 날짜 필터링
selected = df[
    (df["월"] == month) &
    (df["일"] == day)
].copy()

selected = selected.sort_values("연도")

st.subheader(
    f"📈 {month}월 {day}일의 연도별 최고·최저기온"
)

fig = go.Figure()

# 최고기온 (분홍색)
fig.add_trace(
    go.Scatter(
        x=selected["연도"],
        y=selected["최고기온(℃)"],
        mode="lines+markers",
        name="최고기온",
        line=dict(
            color="deeppink",
            width=3
        ),
        marker=dict(
            size=6,
            color="deeppink"
        )
    )
)

# 최저기온 (연한 파란색)
fig.add_trace(
    go.Scatter(
        x=selected["연도"],
        y=selected["최저기온(℃)"],
        mode="lines+markers",
        name="최저기온",
        line=dict(
            color="lightblue",
            width=3
        ),
        marker=dict(
            size=6,
            color="lightblue"
        )
    )
)

fig.update_layout(
    title=f"{month}월 {day}일 연도별 기온 변화",
    xaxis_title="연도",
    yaxis_title="기온 (℃)",
    hovermode="x unified",
    height=650,
    legend=dict(
        title="범례"
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("데이터")

st.dataframe(
    selected[
        [
            "연도",
            "평균기온(℃)",
            "최저기온(℃)",
            "최고기온(℃)"
        ]
    ],
    use_container_width=True
)
