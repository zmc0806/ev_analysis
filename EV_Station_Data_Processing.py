#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
import json
import pandas as pd


# In[3]:


# Load configuration from config.json
with open('config/config.json', 'r') as config_file:
    config = json.load(config_file)

api_key = config['api_key']
base_url = config['base_url']
state = config['state']
fuel_type = config['fuel_type']

# Download JSON data
url = f"{base_url}.json?api_key={api_key}&fuel_type={fuel_type}&state={state}"
response = requests.get(url)

# Check response status
if response.status_code == 200:
    data = response.json()
    # Save as JSON file
    with open('data/alt_fuel_stations.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("The data is successfully downloaded and saved as alt_fuel_stations.json")
else:
    print(f"Request failed, status code: {response.status_code}, error message: {response.text}")

# Download CSV data
csv_url = f"{base_url}.csv?api_key={api_key}&fuel_type={fuel_type}&state={state}"
df = pd.read_csv(csv_url)
df.to_csv('data/alt_fuel_stations.csv', index=False)
print("The data is successfully downloaded and saved as alt_fuel_stations.csv")

# Load SDG&E service territory zip codes
sdge_zipcode = pd.read_excel('data/SDGE Service Territory Zip Code List Q2-2021.xlsx')
zip_codes = ",".join(sdge_zipcode['ZIP_CODE'].astype(str).tolist())

# Build the request URL with filters for fuel type, state, and zip codes
filtered_url = f"{base_url}.json?api_key={api_key}&fuel_type={fuel_type}&state={state}&zip={zip_codes}"

# Request the data in JSON format
response = requests.get(filtered_url)
if response.status_code == 200:
    data = response.json()
    
    # Normalize JSON data to a DataFrame
    stations_df = pd.json_normalize(data['fuel_stations'])
    
    # Save as CSV
    stations_df.to_csv('data/filtered_alt_fuel_stations.csv', index=False)
    print("The filtered data is successfully saved as filtered_alt_fuel_stations.csv")
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")


# In[9]:


import requests
import os

# Define the URL and the save path
url = 'https://energydata.sdge.com/downloadEnergyUsageFile?name=SDGE-ELEC-2024-Q3.csv'
save_path = os.path.join('data', 'SDGE-ELEC-2024-Q3.csv')

# Ensure the target folder exists
os.makedirs('data', exist_ok=True)

# Download the file
response = requests.get(url)

if response.status_code == 200:
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print(f'File successfully downloaded to {save_path}')
else:
    print(f'Failed to download the file. Status code: {response.status_code}')



# In[6]:


import os
import requests

# Define the list of URLs and corresponding file years
urls = [
    'https://data.ca.gov/dataset/15179472-adeb-4df6-920a-20640d02b08c/resource/d304108a-06c1-462f-a144-981dd0109900/download/vehicle-fuel-type-count-by-zip-code.csv',
    'https://data.ca.gov/dataset/15179472-adeb-4df6-920a-20640d02b08c/resource/4254a06d-9937-4083-9441-65597dd267e8/download/vehicle-count-as-of-1-1-2020.csv',
    'https://data.ca.gov/dataset/15179472-adeb-4df6-920a-20640d02b08c/resource/888bbb6c-09b4-469c-82e6-1b2a47439736/download/vehicle-fuel-type-count-by-zip-code-2021.csv',
    'https://data.ca.gov/dataset/15179472-adeb-4df6-920a-20640d02b08c/resource/1856386b-a196-4e7c-be81-44174e29ad50/download/vehicle-fuel-type-count-by-zip-code-2022.csv',
    'https://data.ca.gov/dataset/15179472-adeb-4df6-920a-20640d02b08c/resource/9aa5b4c5-252c-4d68-b1be-ffe19a2f1d26/download/vehicle-fuel-type-count-by-zip-code-2022.csv',
    'https://data.ca.gov/dataset/15179472-adeb-4df6-920a-20640d02b08c/resource/d599c3d3-87af-4e8c-8694-9c01f49e3d93/download/vehicle-fuel-type-count-by-zip-code-20231.csv'
]

years = [2018, 2019, 2020, 2021, 2022, 2023]

# Specify the directory to save files
save_dir = 'data/'

# Create the directory if it does not exist
os.makedirs(save_dir, exist_ok=True)

for url, year in zip(urls, years):
    response = requests.get(url)
    if response.status_code == 200:
        # Use a shortened file name and save it to the 'data' folder
        file_name = os.path.join(save_dir, f'VFT_Count_Zip_{year}.csv')
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File {file_name} downloaded successfully")
    else:
        print(f"Download failed: {url}")

