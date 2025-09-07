# General Imports
import pandas as pd
import os

# Import API clients
import weather_client
import earthquake_client

# Weather Client Tests - Tokyo Station and Kyoto
coordinates = [(35.675163966, 139.766830266), (34.98561, 135.758915)]
weather_uuid = weather_client.get_weather_forcast(coordinates)
weather_filename = f"weather_{weather_uuid}.parquet"
assert os.path.exists(weather_filename), f"{weather_filename} not created"
df = pd.read_parquet(weather_filename)
print(df)

# Earthquake Client Tests
quake_uuid = earthquake_client.get_earthquake_events()
quake_filename = f"earthquake_{quake_uuid}.parquet"
assert os.path.exists(quake_filename), f"{quake_filename} not created"
df = pd.read_parquet(quake_filename)
print(df)