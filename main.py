from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load the dataset
plant_growth = pd.read_csv("Plant Growth.csv")
plant_growth["date"] = pd.to_datetime(plant_growth["date"]).dt.strftime('%Y-%m-%d')

@app.get("/api/plant-growth")
def get_plant_growth():
    return plant_growth.to_dict(orient="records")