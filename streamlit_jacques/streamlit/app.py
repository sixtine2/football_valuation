import streamlit as st

import datetime

import requests

'''
# TaxiFareModel front

This front queries the Le Wagon [taxi fare model API](https://taxifare.lewagon.ai/predict?pickup_datetime=2012-10-06%2012:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2)
'''

pickup_date = st.date_input('pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
pickup_time = st.time_input('pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
pickup_datetime = f'{pickup_date} {pickup_time}'
pickup_longitude = st.number_input('pickup longitude', value=40.7614327)
pickup_latitude = st.number_input('pickup latitude', value=-73.9798156)
dropoff_longitude = st.number_input('dropoff longitude', value=40.6413111)
dropoff_latitude = st.number_input('dropoff latitude', value=-73.7803331)
passenger_count = st.number_input('passenger_count', min_value=1, max_value=8, step=1, value=1)

# enter here the address of your flask api
url = 'https://taxifare.lewagon.ai/predict'

params = dict(
    pickup_datetime=pickup_datetime,
    pickup_longitude=pickup_longitude,
    pickup_latitude=pickup_latitude,
    dropoff_longitude=dropoff_longitude,
    dropoff_latitude=dropoff_latitude,
    passenger_count=passenger_count)

response = requests.get(url, params=params)

prediction = response.json()

pred = prediction['fare']

pred
