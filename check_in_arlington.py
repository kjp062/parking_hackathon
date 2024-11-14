arlington_boundary = {
    "min_lat": 38.8275, # Minimum latitude 
    "max_lat": 38.9339, # Maximum latitude 
    "min_lon": -77.1724, # Minimum longitude 
    "max_lon": -77.0663 # Maximum longitude
}

def check_in_arlington(lat, lon):
    return (arlington_boundary["min_lat"] <= lat <= arlington_boundary["max_lat"] 
            and arlington_boundary["min_lon"] <= lon <= arlington_boundary["max_lon"])