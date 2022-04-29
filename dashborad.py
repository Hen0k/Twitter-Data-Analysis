import streamlit as st
import pandas as pd
import numpy as np

from mysql_manager import get_labled_tweets
from mysql_manager import get_cleaned_tweets

st.title('Twitter Data Analysis')

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
@st.cache
def load_labled_data():
    return get_labled_tweets()

@st.cache
def load_cleaned_data():
    return get_cleaned_tweets()

labled_df = load_labled_data()
cleaned_df = load_cleaned_data()

# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

if st.checkbox('Show Labled Data'):
    st.subheader('Labled Data')
    st.write(labled_df)

if st.checkbox('Show Cleaned Data'):
    st.subheader('Cleaned Data')
    st.write(cleaned_df)

