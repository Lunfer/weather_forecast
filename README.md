# Weather Forecast Application

## Instructions

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd weather_forecast_project

2. **Create and Activate Virtual Environment**

   ```python -m venv .venv
      source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`


3. **Set up the environment variables:**
   - `DATABASE_URL`: Database connection string (default is `sqlite:///weather.db`)

   **Create a .env file in the root directory with the following content:**
   - `API_USERNAME`: Your Meteomatics API username
   - `API_PASSWORD`: Your Meteomatics API password
   

4. **Run the application locally:**
   ```bash
   python app.py
## Access Flask-Admin

Open a browser and navigate to `/admin/`.

## API Endpoints

### List Locations
- **Endpoint:** `/locations`
- **Method:** `GET`
- **Description:** Returns a list of distinct locations.
- **Response:** JSON array of locations.

### Latest Forecast
- **Endpoint:** `/latest_forecast`
- **Method:** `GET`
- **Description:** Returns the latest weather forecast for all locations.
- **Response:** JSON array of forecasts.

### Average Temperature
- **Endpoint:** `/average_temp`
- **Method:** `GET`
- **Description:** Returns the average temperature for each location and date.
- **Response:** JSON array of average temperatures.

### Top Locations
- **Endpoint:** `/top_locations`
- **Method:** `GET`
- **Query Parameter:** `n` (number of top locations to return)
- **Description:** Returns the top `n` locations by average temperature.
- **Response:** JSON array of top locations.

## Troubleshooting Guide

**Issue:** API endpoints return empty results.
**Solution:** Verify that the database is correctly initialized and contains data. Check logs for any errors during data fetch or processing.

**Issue:** Authentication issues with the weather API.
**Solution:** Check that API credentials are correctly set in the `.env` file and match the credentials expected by the API.





