import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(
    page_title="기온 분석",
    layout="wide"
)

st.title("🌡️ 서울 기온 분석")

# --------------------------------------------------
# CSV 불러오기
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
csv_path = BASE_DIR / "seoul.csv"

try:
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
except:
    try:
        df = pd.read_csv(csv_path, encoding="utf-8")
    except:
        df = pd.read_csv(csv_path, encoding="cp949")

# --------------------------------------------------
# 컬럼명 정리
# --------------------------------------------------

df.columns = (
    df.columns
    .str.replace("\ufeff", "", regex=False)
    .str.strip()
)

# --------------------------------------------------
# 날짜 컬럼 찾기
# --------------------------------------------------

date_col = None

for col in df.columns:
    if "날짜" in col:
        date_col = col
        break

if date_col is None:
    st.error(
        f"날짜 컬럼을 찾을 수 없습니다.\n\n현재 컬럼:\n{df.columns.tolist()}"
    )
    st.stop()

# --------------------------------------------------
# 날짜 처리
# --------------------------------------------------

df[date_col] = (
    df[date_col]
    .astype(str)
    .str.strip()
)

df[date_col] = pd.to_datetime(
    df[date_col],
    errors="coerce"
)

df = df.dropna(subset=[date_col])

# --------------------------------------------------
# 연/월/일 생성
# --------------------------------------------------

df["연도"] = df[date_col].dt.year
df["월"] = df[date_col].dt.month
df["일"] = df[date_col].dt.day

# --------------------------------------------------
# 기온 컬럼 찾기
# --------------------------------------------------

max_col = None
min_col = None
avg_col = None

for col in df.columns:

    if "최고기온" in col:
        max_col = col

    elif "최저기온" in col:
        min_col = col

    elif "평균기온" in col:
        avg_col = col

if max_col is None or min_col is None:
    st.error(
        f"기온 컬럼을 찾을 수 없습니다.\n\n현재 컬럼:\n{df.columns.tolist()}"
    )
    st.stop()

# --------------------------------------------------
# 월 선택
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    month = st.selectbox(
        "월 선택",
        sorted(df["월"].unique())
    )

# --------------------------------------------------
# 일 선택
# --------------------------------------------------

with col2:

    days = sorted(
        df[df["월"] == month]["일"].unique()
    )

    day = st.selectbox(
        "일 선택",
        days
    )

# --------------------------------------------------
# 데이터 필터링
# --------------------------------------------------

selected = df[
    (df["월"] == month)
    & (df["일"] == day)
].copy()

selected = selected.sort_values("연도")

# --------------------------------------------------
# 그래프
# --------------------------------------------------

st.subheader(
    f"📈 {month}월 {day}일의 연도별 최고·최저기온"
)

fig = go.Figure()

# 최고기온 (분홍색)

fig.add_trace(
    go.Scatter(
        x=selected["연도"],
        y=selected[max_col],
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
        y=selected[min_col],
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
    legend_title="범례",
    height=650
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# 데이터 표
# --------------------------------------------------

st.subheader("📋 데이터")

show_cols = ["연도"]

if avg_col:
    show_cols.append(avg_col)

show_cols.extend([min_col, max_col])

st.dataframe(
    selected[show_cols],
    use_container_width=True
)
