# import required libraries
import streamlit as st   
from datetime import datetime
from zoneinfo import ZoneInfo


# List of available timezones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "Asia/Kolkata",
    "Asia/Shanghai",
    "Asia/Tokyo",
    "Australia/Sydney",
    "Europe/London",
    "America/New_York",
    "America/Chicago",
    "America/Denver",
    "America/Los_Angeles",
    "Asia/Dubai",
    "Europe/Berlin",
    "Europe/Paris",
    "Europe/Rome",
    "Europe/Madrid",
    "Europe/Amsterdam",
    "Europe/Stockholm",
    "Europe/Oslo",   
]

# app title
st.title("Time Zone App")

# Create a multiselect widget for selecting timezones
selected_timezone = st.multiselect("Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"])

#Display the current time for selected timzones
st.subheader("Selected Timezones")
for tz in selected_timezone:
    
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%n-%d %I %H:%M:%S %p")
    st.write(f"**{tz}**: {current_time}")
 
st.subheader("Convert Time Between Timezones")

current_time = st.time_input("Current Time", value=datetime.now().time())

from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)

to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

if st.button("Convert Time"):
    
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))

    Converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%n-%d %I %H:%M:%S %p")
    
    st.success(f"Converted Time in {to_tz}: {Converted_time}")
    
st.subheader("Timezone Information")

