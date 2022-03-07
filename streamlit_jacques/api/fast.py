# $DELETE_BEGIN
from datetime import datetime
import pytz

import pandas as pd
import joblib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)



''''
test de l'APÏ (sans valeur d'entrée)
'''
@app.get("/")
def index():
    return dict(greeting="start_football_viz")





'''
predict la valeur d'un joueur avec entrée prénom + nom //// déjà waterfall + knn ????
'''


@app.get("/predict")
def predict_price(player_name):       # 1
    # build X ⚠️ beware to the order of the parameters ⚠️
    X = (player_name))

#     # ⚠️ TODO: get model from GCP

    # pipeline = get_model_from_gcp()
    pipeline = joblib.load('model.joblib')

    # make prediction
    results = pipeline.predict(X)

    # convert response from numpy to python type
    pred = float(results[0])

    return dict(fare=pred)




# $DELETE_END




