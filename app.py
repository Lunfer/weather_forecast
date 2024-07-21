# app.py

import requests
import logging
from datetime import datetime, timedelta
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, jsonify, request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import func
from database import SessionLocal, init_db, engine
from models import WeatherForecast
from config import Config
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Debugging: print loaded environment variables
print(f"API_USERNAME: {os.getenv('API_USERNAME')}")
print(f"API_PASSWORD: {os.getenv('API_PASSWORD')}")

# Configure logging
logging.basicConfig(level=logging.INFO)


def fetch_weather_data():
    session = SessionLocal()
    try:
        for location in Config.LOCATIONS:
            end_date = datetime(
                2024, 7, 30
            )  # Example end date within the allowed period
            start_date = end_date - timedelta(days=7)
            dates = [start_date + timedelta(days=i) for i in range(8)]

            for date in dates:
                date_str = date.strftime("%Y-%m-%dT%H:%M:%SZ")
                url = f"https://api.meteomatics.com/{date_str}/t_2m:C/{location}/json"
                try:
                    # Log the credentials for debugging
                    logging.info(f"Using username: {Config.API_USERNAME}")
                    logging.info(f"Using password: {Config.API_PASSWORD}")

                    response = requests.get(
                        url, auth=(Config.API_USERNAME, Config.API_PASSWORD)
                    )

                    # Log the response for debugging
                    logging.info(f"Response status code: {response.status_code}")
                    logging.info(f"Response text: {response.text}")

                    response.raise_for_status()
                    data = response.json()

                    forecast = WeatherForecast(
                        location=location,
                        date=date,
                        temperature=data["data"][0]["coordinates"][0]["dates"][0][
                            "value"
                        ],
                        humidity=None,  # Update if the API provides this data
                        wind_speed=None,  # Update if the API provides this data
                    )
                    session.add(forecast)
                except requests.exceptions.HTTPError as http_err:
                    logging.error(f"HTTP error occurred: {http_err}")
                except requests.exceptions.RequestException as err:
                    logging.error(f"Error occurred: {err}")
                except ValueError as json_err:
                    logging.error(f"JSON decode error: {json_err}")

        session.commit()
    finally:
        session.close()


app = Flask(__name__)

# Setup Flask-Admin
admin = Admin(app, name='Weather Forecast Admin', template_mode='bootstrap3')

# Create a session factory
session_factory = sessionmaker(bind=engine)
# Create a scoped session
scoped_session = scoped_session(session_factory)

# Add views
admin.add_view(ModelView(WeatherForecast, scoped_session))

@app.route("/locations", methods=["GET"])
def list_locations():
    session = SessionLocal()
    locations = session.query(WeatherForecast.location).distinct().all()
    session.close()
    return jsonify([loc[0] for loc in locations])


@app.route("/latest_forecast", methods=["GET"])
def latest_forecast():
    session = SessionLocal()
    results = (
        session.query(WeatherForecast)
        .group_by(WeatherForecast.location, WeatherForecast.date)
        .all()
    )
    session.close()
    return jsonify([forecast.to_dict() for forecast in results])


@app.route("/average_temp", methods=["GET"])
def average_temp():
    session = SessionLocal()
    results = (
        session.query(
            WeatherForecast.location,
            WeatherForecast.date,
            func.avg(WeatherForecast.temperature),
        )
        .group_by(WeatherForecast.location, WeatherForecast.date)
        .all()
    )
    session.close()
    return jsonify(
        [{"location": r[0], "date": r[1], "avg_temp": r[2]} for r in results]
    )


@app.route("/top_locations", methods=["GET"])
def top_locations():
    n = int(request.args.get("n", 10))
    session = SessionLocal()
    results = (
        session.query(
            WeatherForecast.location,
            func.avg(WeatherForecast.temperature).label("avg_temp"),
        )
        .group_by(WeatherForecast.location)
        .order_by(func.avg(WeatherForecast.temperature).desc())
        .limit(n)
        .all()
    )
    session.close()
    return jsonify([{"location": r[0], "avg_temp": r[1]} for r in results])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
