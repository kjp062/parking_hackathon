import pandas as pd

meterData = pd.read_csv("C:\\Users\\keper\\Documents\\Coding\\hackathon\\Parking_Meters.csv")

def get_meter_data():
    return meterData

if __name__ == "__main__":
    print(get_meter_data())