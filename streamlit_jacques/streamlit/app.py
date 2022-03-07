import streamlit as st
import datetime
import requests
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# url to request
url = "https://raw.githubusercontent.com/sixtine2/football_valuation/master/streamlit_jacques/Data/test.csv"
# pretty print JSON data
df = pd.read_csv(url)
df.columns = df.iloc[0]
dict_player = df.loc[df['Player Name'] == 'Zlatan Ibrahimovic'].to_dict(orient='records')[0]

###

player_name = 'Lionel Messi'
player_age = dict_player['age']
position = 'Attack'
games_played = 100
goals = 10
assists = 10
rating = 7.5
contract_expires = 2023
spg = 3
player_face = 'https://cdn.sofifa.net/players/158/023/22_120.png'
club_logo = 'https://cdn.sofifa.net/teams/73/60.png'
nation_logo = 'https://cdn.sofifa.net/teams/1369/60.png'

#st.set_page_config(layout="wide")

st.title(player_name)
#st.image(player_face)
#st.markdown("<img src='https://cdn.sofifa.net/players/158/023/22_120.png'")

st.subheader('Key info:')
col1, col2, col3 = st.columns(3)
col1.metric("Position: ", str(position))
col2.metric("Age: ", str(player_age))
col3.metric("Contract expires in: ", str(contract_expires))

#expander = st.expander('You can click here to see the raw data first 👉')
#expander.dataframe(data=df.loc[df['Player Name'] == 'Zlatan Ibrahimovic'].to_dict(orient='records')[0])

st.subheader('Recent performance snapshot:')
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("🏟️ " + str(games_played) + " Matches")
with col2:
    st.markdown("🥅 " + str(goals) + " Total Goals")
with col3:
    st.markdown("👟⚽ " + str(spg) + " Shots per Game")
with col4:
    st.markdown("🔁" + str(assists) + " Assists per Game")

st.subheader('Market value bridge:')
fig = go.Figure(go.Waterfall(
    name = "20", orientation = "v",
    measure = ["relative", "relative", "total", "relative", "total", "relative", "total"],
    x = ["Sales cut", "Subs revenue", "Total revenue", "Reputational costs", "Profit before IT", "IT costs", "Profit after IT"],
    textposition = "outside",
    text = ["1.4M", "1.5M","2.8M", "-1.4M", "1.4M", "-0.5M", "0.9M"],
    y = [1.4, 1.5, 2.8, -1.4, 1.4, -0.5, -0.5 -0.9],
    connector = {"line":{"color":"rgb(210, 210, 210)"}}
))

fig.update_layout(
        font_family="Helvetica",
        #title = "Profit calculation",
        showlegend = False,
    plot_bgcolor='rgb(255,255,255)'
)
fig.update_layout(yaxis={'visible': False, 'showticklabels': False})
fig.update_layout(xaxis={'visible': True, 'showticklabels': True}, xaxis_title=None)

st.plotly_chart(fig)
