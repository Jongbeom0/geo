import folium

# 서울의 중심 좌표 (예시: 서울시청)
center_coordinates = [37.5665, 126.9780]

# 고등학교 좌표 데이터 (위도, 경도)
high_schools = [
    {"name": "고등학교1", "lat": 37.5701, "lon": 126.9825},
    {"name": "고등학교2", "lat": 37.5728, "lon": 126.9876},
    {"name": "고등학교3", "lat": 37.5760, "lon": 126.9812},
    {"name": "고등학교4", "lat": 37.5683, "lon": 126.9937},
    {"name": "고등학교5", "lat": 37.5625, "lon": 126.9762},
    {"name": "고등학교6", "lat": 37.5591, "lon": 126.9777},
    {"name": "고등학교7", "lat": 37.5582, "lon": 126.9730},
    {"name": "고등학교8", "lat": 37.5637, "lon": 126.9651},
    {"name": "고등학교9", "lat": 37.5711, "lon": 126.9640},
    {"name": "고등학교10", "lat": 37.5764, "lon": 126.9631},
    {"name": "고등학교11", "lat": 37.5810, "lon": 126.9832},
    {"name": "고등학교12", "lat": 37.5669, "lon": 126.9783},
    {"name": "고등학교13", "lat": 37.5647, "lon": 126.9820},
    {"name": "고등학교14", "lat": 37.5682, "lon": 126.9790},
    {"name": "고등학교15", "lat": 37.5612, "lon": 126.9855},
    {"name": "고등학교16", "lat": 37.5679, "lon": 126.9703},
    {"name": "고등학교17", "lat": 37.5743, "lon": 126.9722},
    {"name": "고등학교18", "lat": 37.5776, "lon": 126.9789},
    {"name": "고등학교19", "lat": 37.5809, "lon": 126.9710},
    {"name": "고등학교20", "lat": 37.5610, "lon": 126.9693}
]

# 교육기관 좌표 데이터 (위도, 경도)
education_centers = [
    {"name": "교육기관1", "lat": 37.5665, "lon": 126.9780},
    {"name": "교육기관2", "lat": 37.5693, "lon": 126.9810},
    {"name": "교육기관3", "lat": 37.5716, "lon": 126.9790},
    {"name": "교육기관4", "lat": 37.5740, "lon": 126.9765},
    {"name": "교육기관5", "lat": 37.5765, "lon": 126.9740}
]

# 지도 생성
m = folium.Map(location=center_coordinates, zoom_start=13)

# 고등학교 마커 추가
for school in high_schools:
    folium.Marker(
        location=[school["lat"], school["lon"]],
        popup=school["name"],
        icon=folium.Icon(color='red')
    ).add_to(m)

# 교육기관 마커 추가
for center in education_centers:
    folium.Marker(
        location=[center["lat"], center["lon"]],
        popup=center["name"],
        icon=folium.Icon(color='blue')
    ).add_to(m)

# 지도 저장
m.save('seoul_schools_map.html')