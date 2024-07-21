# Weather Forecast Application

The Weather Forecast Application is a Flask-based web service designed to fetch, store, and analyze weather forecast data. The application provides a RESTful API for retrieving weather information and an administrative interface for managing data. It is deployed on Google Cloud Platform (GCP) using Artifact Registry and Cloud Run for a scalable and efficient cloud deployment.

### Technologies Used
- Flask: A lightweight web framework used for creating the web service and handling HTTP requests.
- Flask-Admin: An extension for Flask that provides a web-based administrative interface for managing the application’s data.
- SQLAlchemy: An Object-Relational Mapper (ORM) used for interacting with the SQLite database.
- Requests: A Python library used to make HTTP requests to the external weather API.
- SQLite: A lightweight database used for storing weather forecast data.
- dotenv: A library used for loading environment variables from a .env file to manage API credentials and other configurations.
- Google Cloud Platform (GCP): Provides the infrastructure for deployment.
  - Artifact Registry: Stores Docker images of the application.
  - Cloud Run: Manages and scales the deployment of the Docker container.
### Deployment
- Artifact Registry: Docker images of the application are built and stored in Google Cloud’s Artifact Registry.
- Cloud Run: The application is deployed from Artifact Registry to Cloud Run, which handles scaling and managing the containerized application.

### Future Enhancements
- Extended Data Integration: Support additional weather metrics such as humidity and wind speed.
- User Authentication: Implement authentication for secure access to the Flask-Admin interface.
- Enhanced Data Visualization: Incorporate graphical data representations for better insights and user experience.

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

5. **Google Cloud Platform Deployment:**

- Artifact Registry:
   - Build a Docker image of the application.
   - Tag the Docker image and push it to Google Cloud Artifact Registry
      ```
      docker build -t gcr.io/PROJECT_ID/weather-forecast-app
      docker push gcr.io/PROJECT_ID/weather-forecast-app
      ```
   - Replace PROJECT_ID with your actual Google Cloud project ID.

- Cloud Run:
   - Deploy the Docker image from Artifact Registry to Google Cloud Run:
   ```
   gcloud run deploy weather-forecast-app \
  --image gcr.io/PROJECT_ID/weather-forecast-app \
  --platform managed \
  --region YOUR_REGION \
  --allow-unauthenticated
  ```
   - Replace YOUR_REGION with the region where you want to deploy.


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

## Code Files
   - `app.py`: The main Flask application script that contains routes, API endpoints, and the Flask-Admin setup. You have provided this script.
   - `database.py`: Contains the SQLAlchemy engine and session setup.
   - `models.py`: Defines the `WeatherForecast` model.
   - `config.py`: Configuration file for environment-specific settings.
   - `query_db.py`: A snippet of code for quering the database manually



