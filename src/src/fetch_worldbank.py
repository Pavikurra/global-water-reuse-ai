import requests
import pandas as pd


def fetch_worldbank_indicator(indicator_code, start_year=2022, end_year=2024):

    url = (
        f"https://api.worldbank.org/v2/country/all/indicator/{indicator_code}"
        f"?format=json&per_page=20000&date={start_year}:{end_year}"
    )

    response = requests.get(url)

    response.raise_for_status()

    data = response.json()

    if len(data) < 2:
        return pd.DataFrame()

    records = data[1]

    rows = []

    for item in records:

        if item["value"] is not None and item["countryiso3code"]:

            rows.append({
                "country": item["country"]["value"],
                "iso3": item["countryiso3code"],
                "year": int(item["date"]),
                indicator_code: item["value"]
            })

    return pd.DataFrame(rows)


if __name__ == "__main__":

    population = fetch_worldbank_indicator("SP.POP.TOTL")

    population.to_csv(
        "data/raw/worldbank_population.csv",
        index=False
    )

    print(population.head())
