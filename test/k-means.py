import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import folium

# Generate random latitude and longitude data for 20 schools in South Korea
np.random.seed(42)
latitude = np.random.uniform(34.0, 38.0, 20)  # South Korea lat range approx 34-38
longitude = np.random.uniform(126.0, 130.0, 20)  # South Korea long range approx 126-130
school_data = pd.DataFrame({'Latitude': latitude, 'Longitude': longitude})

# Function to perform k-means clustering and plot on map
def plot_kmeans_on_map(school_data, k):
    kmeans = KMeans(n_clusters=k, random_state=42)
    school_data['Cluster'] = kmeans.fit_predict(school_data[['Latitude', 'Longitude']])
    
    # Create a map centered around the mean location of the schools
    m = folium.Map(location=[school_data['Latitude'].mean(), school_data['Longitude'].mean()], zoom_start=7)
    
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

# Function to create map with a given k value
def create_school_cluster_map(k):
    m = plot_kmeans_on_map(school_data, k)
    map_path = 'school_clusters_map.html'  # Save in current directory
    m.save(map_path)
    print(f"Map with {k} clusters saved to {map_path}")

# Example usage with k=4
create_school_cluster_map(4)
