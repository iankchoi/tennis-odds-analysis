import pandas as pd

df = pd.read_csv("tennis_matches_2014_2025.csv", usecols=["completed", "best_odds_a", "best_odds_b", "tour", "surface"], low_memory=False)
print(df.shape)

df = df[df["completed"] == 1]
print(df.shape)

df = df.dropna(subset=["best_odds_a", "best_odds_b"])
df = df[df["best_odds_a"] != df["best_odds_b"]]
df["fav_won"] = df["best_odds_a"] < df["best_odds_b"]

print(len(df))
print(df["fav_won"].mean())

df["raw_a"] = 1 / df["best_odds_a"]
df["raw_b"] = 1 / df["best_odds_b"]
df["total"] = df["raw_a"] + df["raw_b"]
df["p_a"] = df["raw_a"] / df["total"]
df["p_b"] = df["raw_b"] / df["total"]
df["fav_prob"] = df[["p_a", "p_b"]].max(axis=1)

print(df["fav_prob"].mean())
print((df["p_a"] + df["p_b"]).mean())
