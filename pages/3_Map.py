import streamlit as st

DATE_COLUMN_MAP = 'date/time'

st.write("# This page will shown Map of all pickups")

hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = st.session_state['uber_data'][st.session_state['uber_data'][DATE_COLUMN_MAP].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)
