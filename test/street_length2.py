import openrouteservice
from openrouteservice import convert

def get_road_distance(api_key, coord1, coord2):
    client = openrouteservice.Client(key=api_key)
    
    # 경로 계산
    routes = client.directions(coordinates=[coord1, coord2], profile='driving-car', format='geojson')
    
    # 도로 거리 추출 (미터 단위)
    distance_meters = routes['features'][0]['properties']['segments'][0]['distance']
    distance_km = distance_meters / 1000  # 킬로미터 단위로 변환
    duration_seconds = routes['features'][0]['properties']['segments'][0]['duration']
    duration_minutes = duration_seconds / 60  # 분 단위로 변환
    
    return distance_km, duration_minutes

# OpenRouteService API 키
api_key = "5b3ce3597851110001cf6248b55180dd962d4bc093ade68d5d9f6c13"

# 두 지점의 위도와 경도를 입력 (예: [경도, 위도])
coord1 = [float(input("첫 번째 지점의 경도를 입력하세요: ")), float(input("첫 번째 지점의 위도를 입력하세요: "))]
coord2 = [float(input("두 번째 지점의 경도를 입력하세요: ")), float(input("두 번째 지점의 위도를 입력하세요: "))]

# 도로 거리 계산
distance, duration = get_road_distance(api_key, coord1, coord2)
print(f"두 지점 사이의 도로 거리는 {distance:.2f} 킬로미터, 예상 소요 시간은 {duration:.2f} 분입니다.")
