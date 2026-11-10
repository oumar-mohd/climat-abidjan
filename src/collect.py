from pathlib import Path

import pandas as pd
import requests

URL = "https://archive-api.open-meteo.com/v1/archive"
PARAMS = {
    "latitude": 5.36,
    "longitude": -4.01,
    "start_date": "2016-01-01",
    "end_date": "2025-12-31",
    "daily": "temperature_2m_max,temperature_2m_min,temperature_2m_mean,precipitation_sum",
    "timezone": "Africa/Abidjan",
}


def collect():
    response = requests.get(URL, params=PARAMS, timeout=60)
    response.raise_for_status()

    df = pd.DataFrame(response.json()["daily"])
    df["time"] = pd.to_datetime(df["time"])

    Path("data/raw").mkdir(parents=True, exist_ok=True)
    df.to_csv("data/raw/abidjan_weather_raw.csv", index=False)
    print(f"{len(df)} jours enregistrés")


if __name__ == "__main__":
    collect()