import pandas as pd

df = pd.read_csv("/Users/shirley/Desktop/players.csv")

df = df.dropna()
df[["draft_year"]] = df[["draft_year"]].apply(pd.to_numeric)
df = df[(df.draft_year >= 1947) & (df.draft_year <= 2018)]
df = df[df["career_FG%"] != '-']
df = df[df["career_FG3%"] != '-']

df.to_csv("/Users/shirley/Desktop/players-clean.csv")