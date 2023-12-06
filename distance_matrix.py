import requests
import pandas as pd
from geocoding import geocode_address

def calculate_distance_matrix(addresses):
    distance_matrix = []
    for address1 in addresses:
        row = []
        for address2 in addresses:
            if address1 == address2:
                row.append(0)
            else:
                row.append(get_distance(address1, address2))
        distance_matrix.append(row)
    return distance_matrix

def get_distance(address1, address2):
    geocoded_address1 = geocode_address(address1)
    geocoded_address2 = geocode_address(address2)
    if geocoded_address1 and geocoded_address2:
        coordinates1 = f"{geocoded_address1['lat']},{geocoded_address1['lon']}"
        coordinates2 = f"{geocoded_address2['lat']},{geocoded_address2['lon']}"
        response = requests.get(f"http://router.project-osrm.org/route/v1/driving/{coordinates1};{coordinates2}?overview=false")
        data = response.json()
        if data['routes']:
            distance = data['routes'][0]['distance']
            return distance
    return None

def save_distance_matrix_to_csv(distance_matrix, addresses):
    df = pd.DataFrame(distance_matrix, columns=addresses, index=addresses)
    df.to_csv('distance_matrix.csv')