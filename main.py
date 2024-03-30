import requests
import pandas as pd
from pprint import pprint

url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

headers = {
	"X-RapidAPI-Key": "e5e3447d44mshf4502313920939cp1e909fjsnbfcdd214acb9",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

seasons = list(range(2010, 2023, 1))

def get_fixtures(seasons):
    findings = []

    for season in seasons:
        params = {"league": "39", "timezone": "America/Cuiaba", "season": str(season)}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        fixtures = data["response"]
        findings.extend(fixtures)
    
    normalized_data = pd.json_normalize(data=findings, sep="_")
    df = pd.DataFrame(normalized_data)

    return df

df = get_fixtures(seasons)

df.to_csv("premier_league_seasons.csv")
