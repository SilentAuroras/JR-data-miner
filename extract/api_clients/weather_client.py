# Weather data API call client

# Request data from JMA weather and earthquake forcast API
#	- https://open-meteo.com/en/docs/jma-api

import uuid
import pandas as pd
import requests_cache
import openmeteo_requests
from retry_requests import retry

def get_weather_forcast(coordinates):
    """
    Fetch weather for a given latitude and longitude using the JMA API
    Args:
        :param coordinates - Tuple of (latitude,longitude)
            Example: [(latitude, longitude), (latitude, longitude)]
        :return: random_uuid
    """

    # Set up the Open-Meteo API client
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=3, backoff_factor=0.2)
    open_meteo = openmeteo_requests.Client(session=retry_session)

    # Setup dataframe for all weather forcast requested, includes multiple lat/long locations
    df = pd.DataFrame()

    # Loop through list of coordinates
    for latitude, longitude in coordinates:

        # Set up the URL and parameters
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": "temperature_2m",
            "models": "jma_seamless",
            "current": [
                "temperature_2m",
                "is_day",
                "precipitation",
                "wind_speed_10m",
                "wind_direction_10m",
            ],
        }

        # Send request to the API
        responses = open_meteo.weather_api(url, params=params)

        # Generate response dictionary
        current = responses[0].Current()
        weather_data = {
            "latitude": latitude,                                   # Provided latitude
            "longitude": longitude,                                 # Provided longitude
            "temperature_2m": current.Variables(0).Value(),         # Current temperature
            "is_day": current.Variables(1).Value(),                 # Current day or night
            "precipitation": current.Variables(2).Value(),          # Current precipitation
            "wind_speed_10m": current.Variables(3).Value(),         # Current wind speed
            "wind_direction_10m": current.Variables(4).Value(),     # Current wind direction
            'timestamp': pd.to_datetime('now')                      # Timestamp for the data
        }

        # Convert the data to a pandas frame
        new_data = pd.DataFrame(weather_data, index=[0])

        # Append to the existing dataframe
        df = pd.concat([df, new_data], ignore_index=True)

    # Generate one single parquet file for this pull of weather data
    # Generate random UUID for parquet storage
    random_uuid = uuid.uuid4()

    # Create parquet file locally
    filename = f"weather_{random_uuid}.parquet"
    df.to_parquet(filename)

    # Return UUID for tracking
    return random_uuid

