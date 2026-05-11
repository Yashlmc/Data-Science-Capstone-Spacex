import requests
import pandas as pd

def get_spacex_data():
    url = "https://api.spacexdata.com/v4/launches/past"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return pd.json_normalize(data)
    else:
        print("Failed to fetch data")
        return None

if __name__ == "__main__":
    df = get_spacex_data()
    if df is not None:
        print(f"Successfully fetched {df.shape[0]} rows.")
        # df.to_csv('../data/raw_api_data.csv', index=False)