import pandas as pd
import questionary
from config import blue_style, path_historical_csv, path_final_csv 
from manually import helpers

df = pd.read_csv(path_historical_csv)
final_df = pd.read_csv(path_final_csv)

choices = helpers.get_choices(df)

answer = questionary.autocomplete(
    "Enter the title:",
    choices=choices,
    ignore_case=True,
    style=blue_style,
    qmark="💠", 
).ask()

clean_title, clean_type = helpers.get_title_type(answer)

# Filter by (Title OR English Title) AND Type
new_row = df[
    ((df["title"] == clean_title) | (df["english_title"] == clean_title)) &
    (df["type"] == clean_type)
].copy()

if new_row["title"].isin(final_df["title"]).any():
    print("This row is already in the df")
else:
    new_row["complete_duration"] = new_row["duration"] * new_row["episodes"]
    final_df = pd.concat([final_df, new_row], ignore_index=True)


final_df.to_csv(path_final_csv, index=False)


