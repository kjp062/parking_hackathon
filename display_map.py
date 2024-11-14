import pandas as pd
import streamlit as st
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
import find_closest_location
import check_in_arlington

st.set_page_config(layout="wide")

st.title("Code the Curb Hackathon")

address = st.text_input("Enter your destination address", value = "Northside Social")
address = address + " Arlington VA"

geolocator = Nominatim(user_agent="ParkingSpotFinder_Hackathon")
location = geolocator.geocode(address)

col1, col2, col3 = st.columns(3, gap="small")

if check_in_arlington.check_in_arlington(location.latitude, location.longitude): 
    if location:
        proximityDf = find_closest_location.find_closest_location((location.latitude, location.longitude))
        proximityDf.rename(columns={"blockfaceID" : "Block Face ID", "coords" : "Coordinates", "stallCount" : "Spots Available", "rate" : "Rate"}, inplace=True)

        top_3_locations = proximityDf.head(3)
        top_3_locations["Distance from Destination"] = top_3_locations["Distance from Destination"].map('{:.2f}mi'.format)
        top_3_locations["Rate"] = top_3_locations["Rate"].map('${:.2f}'.format)

        m = folium.Map(location=[location.latitude, location.longitude], zoom_start=16)
        folium.Marker([location.latitude, location.longitude], tooltip="Destination", icon=folium.Icon(color="red")).add_to(m)
        for _, row in top_3_locations.iterrows():
            folium.Marker(list(row["Coordinates"]), 
                        popup=folium.Popup(f"""
        <p> 
        Distance: {row["Distance from Destination"]}
        <p>
        <p>
        # of Spots: {row["Spots Available"]}
        <p>
        <p>
        Rate: {row["Rate"]}
        <p>
        """, max_width=400),
                        ).add_to(m)
            
        st.dataframe(top_3_locations[["street", "Spots Available", "Distance from Destination", "Rate"]], hide_index=True, use_container_width=True)
        folium_static(m)
    else:
        st.error("Address not found. Please enter a valid address.")
else:
    st.error("Address is not in Arlington. This project is scoped down to only search for Arlington locations.")

