import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="서울 관광지 TOP10",
    layout="wide"
)

st.title("🇰🇷 외국인들이 좋아하는 서울 주요 관광지 TOP10")
st.markdown("폴리움(Folium) 지도로 서울의 인기 관광지를 확인하세요.")

# 서울 중심 좌표
seoul_center = [37.5665, 126.9780]

# 지도 생성
m = folium.Map(
    location=seoul_center,
    zoom_start=11,
    tiles="CartoDB positron"
)

# 관광지 데이터
tourist_spots = [
    {
        "name": "경복궁",
        "lat": 37.5796,
        "lon": 126.9770,
        "desc": "조선 시대의 대표 궁궐"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.5826,
        "lon": 126.9830,
        "desc": "전통 한옥 거리"
    },
    {
        "name": "명동",
        "lat": 37.5637,
        "lon": 126.9827,
        "desc": "쇼핑과 K-뷰티 중심지"
    },
    {
        "name": "남산서울타워",
        "lat": 37.5512,
        "lon": 126.9882,
        "desc": "서울 야경 명소"
    },
    {
        "name": "홍대거리",
        "lat": 37.5563,
        "lon": 126.9220,
        "desc": "젊음과 예술의 거리"
    },
    {
        "name": "인사동",
        "lat": 37.5740,
        "lon": 126.9865,
        "desc": "전통 문화와 기념품 거리"
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "lat": 37.5665,
        "lon": 127.0092,
        "desc": "현대 건축 랜드마크"
    },
    {
        "name": "롯데월드타워",
        "lat": 37.5131,
        "lon": 127.1025,
        "desc": "서울 초고층 랜드마크"
    },
    {
        "name": "한강공원",
        "lat": 37.5207,
        "lon": 126.9395,
        "desc": "서울 시민 휴식 공간"
    },
    {
        "name": "광장시장",
        "lat": 37.5704,
        "lon": 126.9997,
        "desc": "한국 전통 먹거리 시장"
    }
]

# 마커 추가
for idx, spot in enumerate(tourist_spots, start=1):
    folium.Marker(
        location=[spot["lat"], spot["lon"]],
        popup=f"""
        <b>{idx}. {spot['name']}</b><br>
        {spot['desc']}
        """,
        tooltip=spot["name"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 지도 출력
st_folium(m, width=1200, height=700)

# 관광지 리스트
st.subheader("📍 관광지 목록")

for idx, spot in enumerate(tourist_spots, start=1):
    st.write(f"{idx}. {spot['name']} - {spot['desc']}")
