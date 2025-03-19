from fastapi import FastAPI
import pandas as pd
import requests
import io

app = FastAPI()

# GitHub raw file URLs (replace 'your-username' and 'repo-name')
GITHUB_BASE_URL = "https://raw.githubusercontent.com/your-username/atlas-dashboard-backend/main/"

CSV_FILES = {
    "plant_growth": "Plant%20Growth.csv",
    "plant_harvest": "Plant%20Harvest.csv",
    "unit_parameters": "Unit%20Parameters.csv",
    "unit_measurements": "Unit%20Measurements.csv",
    "sun_data": "Sun%20Data.csv",
}

def fetch_csv_data(file_key):
    url = GITHUB_BASE_URL + CSV_FILES[file_key]
    response = requests.get(url)
    response.raise_for_status()
    return pd.read_csv(io.StringIO(response.text))

@app.get("/api/plant-growth")
def get_plant_growth():
    plant_growth = fetch_csv_data("plant_growth")
    plant_growth["date"] = pd.to_datetime(plant_growth["date"]).dt.strftime('%Y-%m-%d')
    return plant_growth.to_dict(orient="records")

@app.get("/api/plant-harvest")
def get_plant_harvest():
    plant_harvest = fetch_csv_data("plant_harvest")
    return plant_harvest.to_dict(orient="records")

@app.get("/api/unit-parameters")
def get_unit_parameters():
    unit_parameters = fetch_csv_data("unit_parameters")
    return unit_parameters.to_dict(orient="records")

@app.get("/api/unit-measurements")
def get_unit_measurements():
    unit_measurements = fetch_csv_data("unit_measurements")
    return unit_measurements.to_dict(orient="records")

@app.get("/api/sun-data")
def get_sun_data():
    sun_data = fetch_csv_data("sun_data")
    return sun_data.to_dict(orient="records")
