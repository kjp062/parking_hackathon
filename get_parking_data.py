import requests as re
import pandas as pd
import json
import pprint

pp = pprint.PrettyPrinter(depth=4)

url = "https://api.exactpark.com/api/v2/arlington/status/zones"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0"}

parkingApiResponse =  re.get(url, headers=headers, timeout=(10, 27))
parkingDict = parkingApiResponse.json()
#print(parkingObject)

#pp.pprint(parkingDict.keys())

parkingDf = pd.DataFrame(parkingDict['data'])
print(parkingDf)