# models.py

from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class WeatherForecast(Base):
    __tablename__ = "weather_forecasts"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, index=True)
    date = Column(DateTime, index=True)
    temperature = Column(Float)
    humidity = Column(Float, nullable=True)
    wind_speed = Column(Float, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "location": self.location,
            "date": self.date.isoformat(),
            "temperature": self.temperature,
            "humidity": self.humidity,
            "wind_speed": self.wind_speed,
        }
