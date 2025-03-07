import folium
import pandas as pd

# Load geocoded data
data = pd.read_csv("crime_data_geocoded.csv")

# Drop rows with missing lat/lon values
data = data.dropna(subset=["latitude", "longitude"])

# Create a base map centered on FSU
crime_map = folium.Map(location=[30.4419, -84.2985], zoom_start=14)

# Add markers with crime details
for _, row in data.iterrows():
    popup_text = f"""
    <b>Crime Type:</b> {row.get('crime_type', 'Unknown')}<br>
    <b>Date:</b> {row.get('crime_date', 'Unknown')}<br>
    <b>Disposition:</b> {row.get('disposition', 'Unknown')}<br>
    """
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=folium.Popup(popup_text, max_width=300),
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(crime_map)

# Save the map
crime_map.save("crime_map.html")
print("Map saved successfully as crime_map.html")
