import pandas as pd
from setup_final import helpers
from config import path_original_airing, path_modified_airing

df = pd.read_csv(path_original_airing, usecols=[2,3,6,7,8,10,11,15,16,18,31,36,52])

# the column "season" has values such as "WINTER 2025", i actually only care about the season and not the year in this column
# this function removes the year from the column
df = helpers.keep_season_only(df, "season")
df["start_date"] = pd.to_datetime(df["start_date"], errors="coerce")
df = df.dropna(subset="start_date")

# this ensures that only airing anime form the past and current season are shown in the anime.csv dataser
df = helpers.filter_season(df)

# this ensures that only VALID_TYPES are shown, go to helpers.py to see which are those types
df = helpers.filter_type(df, "type")
df = helpers.fill_episodes(df)
df = df.drop("next_episode_number", axis=1)
df.to_csv(path_modified_airing, index=False, encoding="utf-8")
