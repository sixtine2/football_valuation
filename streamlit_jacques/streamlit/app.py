import streamlit as st
from multiapp import MultiApp
from apps import player, dataframe

st.set_page_config(
     page_title="Football Valuation",
     page_icon=":soccer:",
     layout="centered",
     initial_sidebar_state="collapsed",
     menu_items={'About': "Ask us about out project: contact details bla bla bla check our GitHub"}
 )

app = MultiApp()
app.add_app("Player Stats", player.app)
app.add_app("Dataframe", dataframe.app)

app.run()
