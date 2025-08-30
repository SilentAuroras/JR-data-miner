import weather_client
import pandas as pd

# Weather Client Tests - Tokyo Station and Kyoto
coordinates = [(35.675163966, 139.766830266), (34.98561, 135.758915)]
created_uuid = weather_client.get_weather_forcast(coordinates)
filename = f"weather_{created_uuid}.parquet"
df = pd.read_parquet(filename)
print(df)