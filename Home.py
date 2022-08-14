import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Uber pickups in NYC")

st.markdown(
    """
 Streamlit is an open-source app framework built specifically for
 Machine Learning and Data Science projects.
 **👈 Select a demo from the sidebar** to see some examples
 of what Streamlit can do!
 ### Want to learn more?
 - Check out [streamlit.io](https://streamlit.io)
 - Jump into our [documentation](https://docs.streamlit.io)
 - Ask a question in our [community
     forums](https://discuss.streamlit.io)
 ### See more complex demos
 - Use a neural net to [analyze the Udacity Self-driving Car Image
     Dataset](https://github.com/streamlit/demo-self-driving)
 - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

if 'uber_data' not in st.session_state:
    st.session_state['uber_data'] = data
