import requests
import pandas as pd

url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

headers = {
	"X-RapidAPI-Key": "e5e3447d44mshf4502313920939cp1e909fjsnbfcdd214acb9",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

params = {"league": "39", "timezone": "America/Cuiaba", "season": "2022"}

request = requests.get(url, headers=headers, params=params)

data = request.json()

fixtures = data["response"]

df = pd.DataFrame(fixtures[:1])

# def decompose_df(df, columns=None, columns_to_explode=None):
#     if columns:
#         for c in columns:
#             df = _decompose_column(df, c)

#     if columns_to_explode:
#         for c in columns_to_explode:
#             df = df.explode(c).copy()
#             df = _decompose_column(df, c)

#     return df

# def _decompose_column(df, column):
#     lk = []
#     for i in df.index:
#         if isinstance(df.loc[i, column], dict):
#             for k in df.loc[i, column].keys():
#                 if k not in lk:
#                     lk.append(k)
#     for k in lk:
#         df[f'{column}_{k}'] = df[column].apply(
#             lambda x: x[k] if isinstance(x, dict) and k in x else '')

#     df.drop(column, axis=1, inplace=True)
#     return df

print(df)

# decomposed_df = decompose_df(df, columns=["fixture", "goals", "league", "teams"], columns_to_explode=None)

# decomposed_df.to_csv("test.csv")

# print(decomposed_df.head())


