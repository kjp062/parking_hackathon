import requests as re
import pandas as pd
import json
import pprint

pp = pprint.PrettyPrinter(depth=4)

url = "https://api.exactpark.com/api/v2/arlington/status/zones"

parkingApiResponse =  re.get(url, timeout=(10, 27))
parkingDict = parkingApiResponse.json()
#print(parkingObject)

#pp.pprint(parkingDict.keys())
def get_parking_data():
    parkingDf = pd.DataFrame(parkingDict['data'])
    return parkingDf

if __name__ == "__main__":
    print(get_parking_data())