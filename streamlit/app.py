import streamlit as st
import pandas as pd
from apps import player

def app():
    st.set_page_config(
        page_title="Home Page",
        page_icon="🤝",
        layout="centered", # wide
        initial_sidebar_state="auto") # collapsed

    # url to request
    url = "https://raw.githubusercontent.com/sixtine2/football_valuation/master/data/final_data_v1.csv"
    df = pd.read_csv(url, sep = ';')
    list_players = list(df['pretty_name'])
    list_title = 'Pick a player please'
    list_players.insert(0, list_title)


    st.title("How fresh is this soccer player ?")

    choice = st.selectbox('', list_players)
    if choice == list_title :
        pass
    else :
     	player.app(choice)

    # dict_player = df.loc[df['Player Name'] == input_name].to_dict(orient='records')[0]

if __name__ == "__main__":
    app()
