import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import folium

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

# Function to create folium map with clusters
def create_folium_map(school_data):
    # Create a map centered around the mean location of the schools
    m = folium.Map(location=[school_data['Latitude'].mean(), school_data['Longitude'].mean()], zoom_start=12)
    
    # Colors for clusters
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 
              'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
              'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',
              'gray', 'black', 'lightgray']
    
    # Add markers to the map
    for idx, row in school_data.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"School {idx+1} (Cluster {int(row['Cluster'])})",
            icon=folium.Icon(color=colors[int(row['Cluster']) % len(colors)])
        ).add_to(m)
    
    return m

# Example usage
k = 4  # Number of clusters (example value)
school_data = perform_kmeans(school_data, k)

# Display the clustering result as a table
print(school_data)

# Create folium map and save as HTML
m = create_folium_map(school_data)
map_path = 'school_clusters_folium_map.html'
m.save(map_path)
print(f"Map with clusters saved as '{map_path}'")
