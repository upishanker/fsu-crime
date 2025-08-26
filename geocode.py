import pandas as pd
import googlemaps
import time

data = pd.read_csv("crime.csv")

API_KEY = ""
gmaps = googlemaps.Client(key=API_KEY)

def get_lat_lon(location):
    try:
        geocode_result = gmaps.geocode(location)
        if geocode_result:
            lat = geocode_result[0]['geometry']['location']['lat']
            lon = geocode_result[0]['geometry']['location']['lng']
            return lat, lon
    except Exception as e:
        print(f"Error geocoding {location}: {e}")
    return None, None

def safe_geocode(location):
    if location in lat_lon_cache:
        return lat_lon_cache[location]
    
    time.sleep(0.1)  
    lat_lon = get_lat_lon(location)
    lat_lon_cache[location] = lat_lon
    return lat_lon

data[['Latitude', 'Longitude']] = data['location'].apply(lambda x: pd.Series(safe_geocode(x)))


data.to_csv("crime_data_geocoded.csv", index=False)
print("Updated file saved as crime_data_geocoded.csv")

