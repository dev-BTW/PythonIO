#This program reads from json file which on web rather than it being stored on local machine

import json
import urllib.request

dataSRC = "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/10/1880-2024/data.json"
with urllib.request.urlopen(dataSRC) as dataStream:
    data = dataStream.read().decode('utf-8')
    anomalies = json.loads(data)

print(anomalies['description'])

for year,value in anomalies['data'].items():
    year,value=int(year),float(value)
    print(f"{year} ... {value:6.2f}")

print("*"*80)