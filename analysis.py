import pandas as pd
# This script analyzes a dataset of chess games stored in a CSV file.
# The dataset includes game results, ratings, and openings.


df = pd.read_csv("games_metadata_profile_2024_01.csv")

print(df.head())

total_games = len(df)

white_wins = len(df[df["Result"] == "1-0"])
black_wins = len(df[df["Result"] == "0-1"])
draws = len(df[df["Result"] == "1/2-1/2"])

print("\nTotal games:", total_games)
print("White win %:", white_wins / total_games * 100)
print("Black win %:", black_wins / total_games * 100)
print("Draw %:", draws / total_games * 100)

# Rating difference (White - Black)
df["rating_diff"] = df["WhiteElo"] - df["BlackElo"]

# Games where White had higher rating
white_higher = df[df["rating_diff"] > 0]

# Win rate when White is higher rated
white_higher_wins = len(white_higher[white_higher["Result"] == "1-0"])

print("\nWhen White is higher rated:")
print("Win %:", white_higher_wins / len(white_higher) * 100)

# Rating difference (White - Black)
df["rating_diff"] = df["WhiteElo"] - df["BlackElo"]

# Games where White had higher rating
white_higher = df[df["rating_diff"] > 0]

# Win rate when White is higher rated
white_higher_wins = len(white_higher[white_higher["Result"] == "1-0"])

print("\nWhen White is higher rated:")
print("Win %:", white_higher_wins / len(white_higher) * 100)

print("\nTop 5 Most Common Openings:")

top_openings = df["Opening"].value_counts().head(5)

for opening, count in top_openings.items():
    print(f"{opening}: {count} games")


print(f"\nTotal games analyzed: {len(df)}")
