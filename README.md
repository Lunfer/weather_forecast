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

## API Endpoints

   - `/locations`: List all unique locations.
   - `/latest_forecast`: Get the latest forecast for each location for every day.
   - `/average_temp`: List the average temperature for the last 3 forecasts for each location for every day.
   - `/top_locations`: Get the top n locations based on average temperature.