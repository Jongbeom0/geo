import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import requests
import json

# Generate random latitude and longitude data for 40 schools in Seoul
np.random.seed(42)
latitude = np.random.uniform(37.4, 37.7, 40)  # Seoul lat range approx 37.4-37.7
longitude = np.random.uniform(126.8, 127.2, 40)  # Seoul long range approx 126.8-127.2
school_data = pd.DataFrame({'Latitude': latitude, 'Longitude': longitude})

# Function to perform k-means clustering
def perform_kmeans(school_data, k):
    kmeans = KMeans(n_clusters=k, random_state=42)
    school_data['Cluster'] = kmeans.fit_predict(school_data[['Latitude', 'Longitude']])
    return school_data

# Function to create V-World map with clusters
def create_vworld_map(school_data, api_key):
    # Base URL for V-World API
    base_url = 'http://api.vworld.kr/req/image'

    # Colors for clusters
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 
              'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
              'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',
              'gray', 'black', 'lightgray']
    
    # Create markers for each school
    markers = []
    for idx, row in school_data.iterrows():
        marker = {
            "type": "Marker",
            "x": row['Longitude'],
            "y": row['Latitude'],
            "text": f"School {idx+1} (Cluster {int(row['Cluster'])})",
            "icon": {
                "style": "pin",
                "color": colors[int(row['Cluster']) % len(colors)]
            }
        }
        markers.append(marker)

    # Create map request payload
    payload = {
        "key": api_key,
        "service": "image",
        "request": "GetMap",
        "format": "png",
        "size": "800,600",
        "bminx": min(longitude),
        "bminy": min(latitude),
        "bmaxx": max(longitude),
        "bmaxy": max(latitude),
        "markers": markers
    }

    # Make request to V-World API
    response = requests.get(base_url, params=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        with open("school_clusters_vworld_map.png", "wb") as f:
            f.write(response.content)
        print("Map with clusters saved as 'school_clusters_vworld_map.png'")
    else:
        print("Error occurred while fetching the map:", response.status_code, response.text)

# Example usage
k = 4  # Number of clusters (example value)
api_key = '27F7217A-0326-38B2-BC9D-BE196967A132'  # Replace with your V-World API key
school_data = perform_kmeans(school_data, k)

# Display the clustering result as a table
print(school_data)

create_vworld_map(school_data, api_key)
