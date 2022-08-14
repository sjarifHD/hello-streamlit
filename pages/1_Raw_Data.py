import streamlit as st

st.set_page_config(
    page_title="Raw Data",
)

st.write("# This page will shown raw data")

st.subheader('Raw data')
st.write(st.session_state['uber_data'])
