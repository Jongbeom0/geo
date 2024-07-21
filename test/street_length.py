import requests

def get_road_distance(api_key, start_coord, end_coord):
    url = "http://api.vworld.kr/req/routing"
    
    params = {
        'service': 'routing',
        'request': 'GetRoute',
        'version': '2.0',
        'format': 'json',
        'apiKey': api_key,
        'start': f'{start_coord[1]},{start_coord[0]}',  # (위도, 경도) 순서
        'end': f'{end_coord[1]},{end_coord[0]}'         # (위도, 경도) 순서
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if data['response']['status'] == 'OK':
        distance_meters = data['response']['result']['featureCollection']['features'][0]['properties']['totalDistance']
        duration_seconds = data['response']['result']['featureCollection']['features'][0]['properties']['totalTime']
        distance_km = distance_meters / 1000  # 킬로미터로 변환
        duration_minutes = duration_seconds / 60  # 분으로 변환
        return distance_km, duration_minutes
    else:
        return None, None

# V-World API 키
api_key = "27F7217A-0326-38B2-BC9D-BE196967A132"

# 두 지점의 위도와 경도 입력
start_lat = float(input("첫 번째 지점의 위도를 입력하세요: "))
start_lon = float(input("첫 번째 지점의 경도를 입력하세요: "))
end_lat = float(input("두 번째 지점의 위도를 입력하세요: "))
end_lon = float(input("두 번째 지점의 경도를 입력하세요: "))

start_coord = (start_lat, start_lon)
end_coord = (end_lat, end_lon)

# 도로 거리 계산
distance, duration = get_road_distance(api_key, start_coord, end_coord)
if distance is not None and duration is not None:
    print(f"두 지점 사이의 도로 거리는 {distance:.2f} 킬로미터, 예상 소요 시간은 {duration:.2f} 분입니다.")
else:
    print("도로 거리를 계산할 수 없습니다. 입력 값을 확인하세요.")
