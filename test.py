## %

import requests
import pandas as pd
from pprint import pprint

## %

url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

headers = {
	"X-RapidAPI-Key": "e5e3447d44mshf4502313920939cp1e909fjsnbfcdd214acb9",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

## %

params_2011 = {"league": "39", "timezone": "America/Cuiaba", "season": "2011"}

response_2011 = requests.get(url, headers=headers, params=params_2011)
data_2011 = response_2011.json()
fixtures_2011 = data_2011["response"]

params_2012 = {"league": "39", "timezone": "America/Cuiaba", "season": "2012"}

response_2012 = requests.get(url, headers=headers, params=params_2012)
data_2012 = response_2012.json()
fixtures_2012 = data_2012["response"]

params_2013 = {"league": "39", "timezone": "America/Cuiaba", "season": "2013"}

response_2013 = requests.get(url, headers=headers, params=params_2013)
data_2013 = response_2013.json()
fixtures_2013 = data_2013["response"]



## %
