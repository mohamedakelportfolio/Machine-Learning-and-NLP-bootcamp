import pickle
import numpy as np
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel, conlist

census_app = FastAPI(title="census_income predicting")


class CensusIncome(BaseModel):
    batches: List[conlist(item_type=int, min_items=92, max_items=92)]
    

@census_app.on_event("startup")
def load_model():
    # Load classifier from pickle file
    with open("/app/census.pkl", "rb") as model:
        global rf_model
        rf_model = pickle.load(model)


@census_app.get("/")
def home():
    return "Congratulations! Your API is working as expected. Now head over to http//localhost80/docs"


@census_app.post("/predict")
def predict(census_income: CensusIncome):
    
    batches = census_income.batches
    np_batches = np.array(batches)
    
    pred = rf_model.predict(np_batches).tolist()
    
    return {"Prediction": pred}