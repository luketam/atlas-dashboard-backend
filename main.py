from fastapi import FastAPI
import pandas as pd
import requests
import io

app = FastAPI()

# GitHub raw file URLs (replace 'your-username' and 'repo-name')
GITHUB_BASE_URL = "https://raw.githubusercontent.com/luketam/atlas-dashboard-backend/main/"

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
    df = pd.read_csv(io.StringIO(response.text), encoding="utf-8")

    # Handle missing values
    df.fillna("", inplace=True)

    return df.to_dict(orient="records")


@app.get("/api/plant-growth")
def get_plant_growth():
    return fetch_csv_data("plant_growth")


@app.get("/api/plant-harvest")
def get_plant_harvest():
    return fetch_csv_data("plant_harvest")


@app.get("/api/unit-parameters")
def get_unit_parameters():
    return fetch_csv_data("unit_parameters")


@app.get("/api/unit-measurements")
def get_unit_measurements():
    return fetch_csv_data("unit_measurements")


@app.get("/api/sun-data")
def get_sun_data():
    return fetch_csv_data("sun_data")