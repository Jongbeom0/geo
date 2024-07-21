import pandas as pd
import folium
from sklearn.cluster import KMeans

# Function to perform k-means clustering and plot the results on a map
def kmeans_clustering_map(file_path, n_clusters):
    # Load the data
    data = pd.read_csv(file_path)
    coordinates = data[['위도', '경도']]

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    data['Cluster'] = kmeans.fit_predict(coordinates)
    
    # Create a map centered around the average coordinates
    m = folium.Map(location=[data['위도'].mean(), data['경도'].mean()], zoom_start=12)
    
    # Define a color map for the clusters
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 
              'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 
              'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']
    
    # Add points to the map
    for idx, row in data.iterrows():
        folium.CircleMarker(
            location=(row['위도'], row['경도']),
            radius=5,
            color=colors[row['Cluster'] % len(colors)],
            fill=True,
            fill_color=colors[row['Cluster'] % len(colors)],
            fill_opacity=0.6,
            popup=row['학교명']
        ).add_to(m)
    
    # Save the map to an HTML file
    map_file_path = f'C:/code/geo/test/busan_schools_clusters_{n_clusters}.html'
    m.save(map_file_path)

    # Create a DataFrame with the cluster details
    cluster_details = data[['학교명', 'Cluster']].sort_values(by='Cluster')
    
    # Save the cluster details to a CSV file
    cluster_details_file_path = f'C:/code/geo/test/busan_schools_clusters_{n_clusters}_details.csv'
    cluster_details.to_csv(cluster_details_file_path, index=False)
    
    # Return paths to the map and the cluster details
    return map_file_path, cluster_details_file_path

# Example usage with 6 clusters
file_path = "C:/code/geo/test/busan.csv"
map_file = kmeans_clustering_map(file_path, 6)
map_file

