import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="서울 기온 분석",
    layout="wide"
)

st.title("🌡️ 서울 기온 연도별 비교")

uploaded_file = st.file_uploader(
    "서울 기온 CSV 파일 업로드",
    type=["csv"]
)

if uploaded_file is not None:

    # CSV 읽기
    try:
        df = pd.read_csv(uploaded_file, encoding="cp949")
    except:
        df = pd.read_csv(uploaded_file, encoding="utf-8")

    # 날짜 변환
    df["날짜"] = pd.to_datetime(df["날짜"])

    # 연도, 월, 일 생성
    df["연도"] = df["날짜"].dt.year
    df["월"] = df["날짜"].dt.month
    df["일"] = df["날짜"].dt.day

    st.success("데이터를 불러왔습니다.")

    col1, col2 = st.columns(2)

    with col1:
        month = st.selectbox(
            "월 선택",
            sorted(df["월"].unique())
        )

    with col2:
        days = sorted(
            df[df["월"] == month]["일"].unique()
        )

        day = st.selectbox(
            "일 선택",
            days
        )

    # 선택된 날짜 데이터
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
                size=7,
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
                size=7,
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

else:
    st.info("CSV 파일을 업로드하세요.")
