import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="드라마 배우 분석",
    layout="wide"
)

# ---------------------------
# 데이터
# ---------------------------
data = [
    # 남자
    ["남자","지창욱","백스트리트 루키","로맨틱코미디",2020],
    ["남자","지창욱","도시남녀의 사랑법","로맨스",2020],
    ["남자","안효섭","낭만닥터 김사부2","의학",2020],
    ["남자","유연석","슬기로운 의사생활","의학",2020],

    ["남자","안효섭","홍천기","판타지 사극",2021],
    ["남자","유연석","슬기로운 의사생활 시즌2","의학",2021],

    ["남자","지창욱","안나라수마나라","판타지",2022],
    ["남자","지창욱","당신이 소원을 말하면","휴먼",2022],
    ["남자","안효섭","사내맞선","로맨틱코미디",2022],
    ["남자","유연석","사랑의 이해","멜로",2022],

    ["남자","지창욱","최악의 악","범죄 액션",2023],
    ["남자","안효섭","너의 시간 속으로","판타지 로맨스",2023],
    ["남자","유연석","운수 오진 날","스릴러",2023],

    ["남자","유연석","지금 거신 전화는","미스터리 로맨스",2024],

    # 여자
    ["여자","채수빈","반의반","로맨스",2020],

    ["여자","김고은","유미의 세포들","로맨틱코미디",2021],
    ["여자","한소희","알고있지만","로맨스",2021],
    ["여자","한소희","마이 네임","액션 느와르",2021],

    ["여자","채수빈","너와 나의 경찰수업","청춘 로맨스",2022],
    ["여자","김고은","유미의 세포들2","로맨틱코미디",2022],
    ["여자","김고은","작은 아씨들","미스터리",2022],
    ["여자","한소희","사운드트랙 #1","로맨스",2022],

    ["여자","한소희","경성크리처","판타지 스릴러",2023],

    ["여자","채수빈","지금 거신 전화는","미스터리 로맨스",2024],
]

df = pd.DataFrame(
    data,
    columns=["구분","배우","드라마","장르","연도"]
)

st.title("🎬 2020~2026 드라마 배우 분석")

# ==================================================
# 연도별 순위
# ==================================================
st.header("🏆 연도별 출연작 순위")

year = st.selectbox(
    "연도 선택",
    sorted(df["연도"].unique())
)

rank_df = (
    df[df["연도"] == year]
    .groupby(["구분","배우"])
    .size()
    .reset_index(name="출연작수")
    .sort_values("출연작수", ascending=False)
    .reset_index(drop=True)
)

rank_df.insert(0, "순위", rank_df.index + 1)

st.dataframe(
    rank_df,
    use_container_width=True,
    hide_index=True
)

# ==================================================
# 남자 배우
# ==================================================
tab1, tab2 = st.tabs(["👨 남자 배우", "👩 여자 배우"])

with tab1:

    male_df = df[df["구분"] == "남자"]

    actor = st.selectbox(
        "남자 배우 선택",
        sorted(male_df["배우"].unique())
    )

    actor_df = male_df[male_df["배우"] == actor]

    st.subheader(f"{actor} 출연작")

    st.dataframe(
        actor_df,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("🎭 장르")

    genres = actor_df["장르"].unique()

    cols = st.columns(len(genres))

    for col, genre in zip(cols, genres):
        col.metric(
            label="장르",
            value=genre
        )

# ==================================================
# 여자 배우
# ==================================================
with tab2:

    female_df = df[df["구분"] == "여자"]

    actor = st.selectbox(
        "여자 배우 선택",
        sorted(female_df["배우"].unique())
    )

    actor_df = female_df[female_df["배우"] == actor]

    st.subheader(f"{actor} 출연작")

    st.dataframe(
        actor_df,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("🎭 장르")

    genres = actor_df["장르"].unique()

    cols = st.columns(len(genres))

    for col, genre in zip(cols, genres):
        col.metric(
            label="장르",
            value=genre
        )

# ==================================================
# 전체 통계
# ==================================================
st.header("📊 전체 배우 출연작 순위")

total_rank = (
    df.groupby(["구분","배우"])
    .size()
    .reset_index(name="출연작수")
    .sort_values("출연작수", ascending=False)
    .reset_index(drop=True)
)

total_rank.insert(0, "순위", total_rank.index + 1)

st.dataframe(
    total_rank,
    use_container_width=True,
    hide_index=True
)
