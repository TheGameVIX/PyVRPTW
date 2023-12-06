```python
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import csv

geolocator = Nominatim(user_agent="geoapiExercises")

def geocode_address(address):
    try:
        return geolocator.geocode(address)
    except GeocoderTimedOut:
        return geocode_address(address)

def cache_geocodes(df, geocoded_cache='geocoded_cache.csv', failed_to_geocode='failed_to_geocode.csv'):
    geocoded_addresses = []
    failed_addresses = []

    for _, row in df.iterrows():
        address = f"{row['Address']}, {row['City']}, {row['State']}, {row['Zip Code']}"
        location = geocode_address(address)
        if location:
            geocoded_addresses.append((address, location.latitude, location.longitude))
        else:
            failed_addresses.append(address)

    with open(geocoded_cache, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(geocoded_addresses)

    with open(failed_to_geocode, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(failed_addresses)

def handle_failed_geocodes(failed_to_geocode='failed_to_geocode.csv'):
    with open(failed_to_geocode, 'r') as f:
        reader = csv.reader(f)
        failed_addresses = list(reader)

    return failed_addresses
```