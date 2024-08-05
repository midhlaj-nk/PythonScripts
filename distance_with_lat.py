import math

def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    # Radius of the Earth in kilometers
    radius_earth_km = 6371
    distance = radius_earth_km * c

    return distance

# Example usage
lat1 = 11.128940
lon1 = 75.895081
lat2 = -23.622681
lon2 = -46.771172

distance = haversine(lat1, lon1, lat2, lon2)
print("Distance:", distance, "km")
