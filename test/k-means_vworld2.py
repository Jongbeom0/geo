import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

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

# Function to create HTML file with V-World map and clusters
def create_vworld_map_html(school_data, api_key, filename='school_clusters_vworld_map.html'):
    # Start of the HTML file
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>School Clusters Map</title>
        <script type="text/javascript" src="https://map.vworld.kr/js/vworldMapInit.js.do?apiKey={api_key}&domain=www.kofac.re.kr"></script>
    </head>
    <body>
        <div id="map" style="width: 100%; height: 600px;"></div>
        <script>
            var map = new vworld.Map("map", {{
                basemapType: vworld.BasemapType.GRAPHIC,
                controlDensity: vworld.DensityType.FULL,
                interaction: vworld.InteractionType.ALL,
                controlsAutoArrange: true,
                homePosition: vworld.PositionType.LATLNG,
                initPosition: vworld.PositionType.LATLNG,
                initZoom: 12
            }});

            var markers = {{}};
    """

    # Colors for clusters
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 
              'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
              'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',
              'gray', 'black', 'lightgray']
    
    # Add markers to the HTML content
    for idx, row in school_data.iterrows():
        color = colors[int(row['Cluster']) % len(colors)]
        html_content += f"""
            markers[{idx}] = new vworld.Marker({{
                position: new vworld.LatLng({row['Latitude']}, {row['Longitude']}),
                icon: new vworld.Icon({{
                    src: 'http://map.vworld.kr/images/poi/pin_{color}.png',
                    size: new vworld.Size(32, 32)
                }}),
                popup: new vworld.Popup({{
                    content: 'School {idx+1} (Cluster {int(row['Cluster'])})'
                }})
            }});
            map.addMarker(markers[{idx}]);
        """

    # End of the HTML file
    html_content += """
        </script>
    </body>
    </html>
    """

    # Save the HTML content to a file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Map with clusters saved as '{filename}'")

# Example usage
k = 4  # Number of clusters (example value)
api_key = '27F7217A-0326-38B2-BC9D-BE196967A132'  # Replace with your V-World API key
school_data = perform_kmeans(school_data, k)

# Display the clustering result as a table
print(school_data)

# Create V-World map and save as HTML
create_vworld_map_html(school_data, api_key)
