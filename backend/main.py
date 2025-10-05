from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
import requests

app = FastAPI(title="Will It Rain On My Parade?")

# Разрешаем фронтенд работать с backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # локально можно *
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ======= функции получения данных =======
def fetch_open_meteo(lat: float, lon: float, days_ahead: int):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&daily=precipitation_probability_mean,temperature_2m_max,temperature_2m_min"
        f"&timezone=auto&forecast_days={min(days_ahead + 1, 16)}"
    )
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

def fetch_nasa_climate(lat: float, lon: float, month: int):
    url = (
        f"https://power.larc.nasa.gov/api/temporal/climatology/point?"
        f"parameters=T2M,T2M_MAX,T2M_MIN,PRECTOT"
        f"&community=RE&longitude={lon}&latitude={lat}"
        f"&format=JSON"
    )
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    try:
        return {
            "temperature_max": data["properties"]["parameter"]["T2M_MAX"][month],
            "temperature_min": data["properties"]["parameter"]["T2M_MIN"][month],
            "precipitation_mm": data["properties"]["parameter"]["PRECTOT"][month]
        }
    except Exception:
        return None

# ======= основной роут =======
@app.get("/forecast")
def get_forecast(
    lat: float = Query(..., description="Latitude"),
    lon: float = Query(..., description="Longitude"),
    date: str = Query(..., description="Target date in YYYY-MM-DD")
):
    today = datetime.utcnow().date()

    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return {"error": "Invalid date format. Use YYYY-MM-DD"}

    days_ahead = (target_date - today).days
    if days_ahead < 0:
        return {"error": "Date cannot be in the past"}

    if days_ahead <= 100:
        data = fetch_open_meteo(lat, lon, days_ahead)
        if not data or "daily" not in data:
            return {"error": "Failed to fetch forecast from Open-Meteo"}

        times = data["daily"]["time"]
        if date not in times:
            date = times[-1]
        index = times.index(date)

        return {
            "source": "Open-Meteo (real forecast)",
            "date": date,
            "latitude": lat,
            "longitude": lon,
            "temperature_max": data["daily"]["temperature_2m_max"][index],
            "temperature_min": data["daily"]["temperature_2m_min"][index],
            "rain_probability_percent": data["daily"]["precipitation_probability_mean"][index],
        }
    else:
        month = target_date.month
        data = fetch_nasa_climate(lat, lon, month)
        if not data:
            return {"error": "Failed to fetch climate data from NASA POWER"}

        rain_prob = min(round(data["precipitation_mm"] * 5), 100)

        return {
            "source": "NASA POWER (climatology estimate)",
            "date": date,
            "latitude": lat,
            "longitude": lon,
            "temperature_max": round(data["temperature_max"], 1),
            "temperature_min": round(data["temperature_min"], 1),
            "rain_probability_percent": rain_prob,
            "message": "This is an approximate long-term climate estimate, not a real forecast."
        }
