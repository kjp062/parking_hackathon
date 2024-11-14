import pandas as pd
import get_parking_data
import get_meter_data
import json

parkingDf = get_parking_data.get_parking_data()
meterDf = get_meter_data.get_meter_data()

def clean_and_join_data():
    meterDf.rename(columns = {"BlockFaceID":"blockfaceID"}, inplace=True)

    joinDf = pd.merge(parkingDf, meterDf, on='blockfaceID', how='left')

    coreDf = joinDf.filter(['stallID',
    'stallName',
    'blockfaceID',
    'status',
    'location',
    'payloadTimestamp',
    'Status',
    'Rate',
    'Latitude',
    'Longitude',
    'Street',
    'PerformanceParking'], axis=1)

    coreDf.rename(columns={"status" : "occupiedStatus", "Status" : "activeStatus"}, inplace=True)
    
    locationDf = pd.json_normalize(coreDf["location"])
    coreDf = coreDf.drop(columns = "location").join(locationDf)

    filteredDf = coreDf[coreDf["PerformanceParking"] == "Yes"]
    filteredDf = filteredDf[coreDf["activeStatus"] == "Active"]
    filteredDf = filteredDf[coreDf["occupiedStatus"] == "vacant"]
    
    filteredDf["Rate"] = filteredDf["Rate"].apply(pd.to_numeric)

    filteredDf['Rate'] = filteredDf.groupby(
    ['stallID',
    'stallName',
    'blockfaceID',
    'occupiedStatus',
    'lat',
    'long',
    'activeStatus',
    'Rate',
    'Street',
    'PerformanceParking'], as_index=False
                      )['Rate'].transform('mean')

    filteredDf = filteredDf.drop_duplicates(subset="stallID", keep="first")

    filteredDf = filteredDf.groupby("blockfaceID", as_index=False).agg(
        stallCount=("stallID", "size"),
        rate=("Rate", "first"),
        lat=("lat", "first"),
        long=("long", "first"),
        street=("Street", "first"))
    
    return filteredDf

if __name__ == "__main__":
    print(clean_and_join_data())