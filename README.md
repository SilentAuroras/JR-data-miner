# JR Data Miner

This repository creates a local data pipeline architecture for analyzing JR (Japan Railways Group) train data using a local Kubernetes deployment. This setup helps perform analysis of JR train operations, schedules, delays by reviewing factors such as weather or earthquakes.

The following data sources are integrated into the pipeline:

-   Station data:
    - API: http://overpass-api.de/
    - Requested data
      - Station name
      - Latitude
      - Longitude
-   Train information (TODO)
-   Earthquake data (TODO)
-   Weather data:
    - API: https://open-meteo.com/en/docs/jma-api
    - Requested data
      - Temperature
      - Day or night
      - Precipitation
      - Wind speed
      - Wind direction

Software Stack Overview:

-   Infrastructure: (TODO)
-   Data Processing: (TODO)
-   Storage: (TODO)
-   Frontend: (TODO)
