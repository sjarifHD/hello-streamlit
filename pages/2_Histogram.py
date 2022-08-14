import streamlit as st
import numpy as np

DATE_COLUMN_HIST = 'date/time'

st.write("# This page will shown histogram number of pickups by hour")
hist_values = np.histogram(
    st.session_state['uber_data'][DATE_COLUMN_HIST].dt.hour, bins=24, range=(0, 24))[0]

st.bar_chart(hist_values)
