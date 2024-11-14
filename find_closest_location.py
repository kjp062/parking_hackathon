import pandas as pd
import clean_and_join_data

from geopy.distance import geodesic
import haversine as hs
from haversine import Unit

df = clean_and_join_data.clean_and_join_data()

northside_coords = (38.885419, -77.097885) # use for testing

def find_closest_location(destination_coords):
    location_data = []

    for index, location in df.iterrows(): 
        coords = (location["lat"], location["long"]) 
        distance = hs.haversine(destination_coords, coords, unit=Unit.MILES) 
        location_data.append((location["blockfaceID"], coords, distance, location["stallCount"], location["rate"], location["street"]))

    locationDf = pd.DataFrame(location_data, columns=["blockfaceID", "coords", "Distance from Destination", "stallCount", "rate", "street"])
    locationDf = locationDf.sort_values(by='Distance from Destination')
    locationDf["Rank by Distance"] = locationDf["Distance from Destination"].rank(method='first')

    return locationDf

if __name__ == "__main__":
    print(find_closest_location(northside_coords))