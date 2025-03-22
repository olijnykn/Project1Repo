import streamlit as st
import requests
import pandas as pd

resp = requests.get('https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date=20250101&end_date=20251231&station=8518750&product=hourly_height&datum=MLLW&time_zone=lst&units=metric&application=DataAPI_Sample&format=json')
df = pd.DataFrame(resp.json()['data'])

st.dataframe(df.head())
