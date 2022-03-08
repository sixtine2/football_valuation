import streamlit as st
import datetime
import requests
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
     page_title="Player Details",
     page_icon=":soccer:",
     layout="centered",
     initial_sidebar_state="collapsed",
     menu_items={'About': "Ask us about out project: contact details bla bla bla check our GitHub"}
 )

input_name = 'Lionel Messi'

def app():

    # url to request
    url = "https://raw.githubusercontent.com/sixtine2/football_valuation/master/streamlit_jacques/Data/test.csv"
    # pretty print JSON data
    df = pd.read_csv(url)
    df.columns = df.iloc[0]
    dict_player = df.loc[df['Player Name'] == 'Lionel Messi'].to_dict(orient='records')[0]

    ###

    player_age = dict_player['age']
    position = 'Attack'
    games_played = dict_player['Games']
    goals = dict_player['Goals']
    assists = dict_player['Assists']
    rating = dict_player['Rating']
    contract_expires = int(dict_player['club_contract_valid_until']) + 2022
    spg = dict_player['SpG']
    key_passes = dict_player['Key Passes']
    dribbles = dict_player['Dribbles']
    fouled = dict_player['Fouled']
    market_value = 60_000_000

    player_face = 'https://cdn.sofifa.net/players/158/023/22_120.png'
    club_logo = 'https://cdn.sofifa.net/teams/73/60.png'
    nation_logo = 'https://cdn.sofifa.net/teams/1369/60.png'

    #st.set_page_config(layout="wide")
    st.markdown("<h1 style='text-align: center; color: #922B21;'>{}</h1>".format(input_name), unsafe_allow_html=True)

    col1, col2, col3 = st.columns([8, 5, 8])
    with col1:
        st.write("")
    with col2:
        st.image(player_face, use_column_width=True)
    with col3:
        st.write("")


    #st.image(player_face)
    #st.image(club_logo)
    #st.markdown("<img src='https://cdn.sofifa.net/players/158/023/22_120.png'")

    st.subheader('Key info:')
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Position: ", str(position))
    col2.metric("Age: ", str(player_age))
    col3.metric("Contract expires in: ", str(contract_expires))
    col4.metric("Market value: ", "€" + str(market_value/1_000_000).format('{:,.0f}') + "M", '+5% vs. average')

    #expander = st.expander('You can click here to see the raw data first 👉')
    #expander.dataframe(data=df.loc[df['Player Name'] == 'Zlatan Ibrahimovic'].to_dict(orient='records')[0])

    st.subheader('Recent performance snapshot:')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("🏟️ " + str(games_played) + " Matches")
    with col2:
        st.markdown("🥅 " + str(goals) + " Total Goals")
    with col3:
        st.markdown("⚽" + str(assists) + " Assists per Game")
    with col4:
        st.markdown("💯" + str(rating) + " Average Rating")


    if position == 'Attack':
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("👟 " + str(spg) + " Shots per Game")
        with col2:
            st.markdown("🔁 " + str(key_passes) + " Key Passes")
        with col3:
            st.markdown("🏃🏽" + str(dribbles) + " Dribbles")
        with col4:
            st.markdown("🤹‍♂️" + str(fouled) + " Fouled")

    elif position == 'Midfield':
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("🏟️ " + str(games_played) + " Matches")
        with col2:
            st.markdown("🥅 " + str(goals) + " Total Goals")
        with col3:
            st.markdown("👟⚽ " + str(spg) + " Shots per Game")
        with col4:
            st.markdown("🔁" + str(assists) + " Assists per Game")

    elif position == 'Defender':
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("🏟️ " + str(games_played) + " Matches")
        with col2:
            st.markdown("🥅 " + str(goals) + " Total Goals")
        with col3:
            st.markdown("👟⚽ " + str(spg) + " Shots per Game")
        with col4:
            st.markdown("🔁" + str(assists) + " Assists per Game")

    else:
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

if __name__ == "__main__":
     app()
