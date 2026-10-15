import pandas as pd

df = pd.read_csv("tennis_matches_2014_2025.csv", low_memory=False)
print(df.shape)

df = df[df["completed"] == 1]
print(df.shape)

df = df.dropna(subset=["best_odds_a", "best_odds_b"])
df = df[df["best_odds_a"] != df["best_odds_b"]]
df["fav_won"] = df["best_odds_a"] < df["best_odds_b"]

print(len(df))
print(df["fav_won"].mean())