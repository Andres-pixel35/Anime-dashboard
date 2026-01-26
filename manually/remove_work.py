import pandas as pd
import questionary
from config import blue_style, path_final_csv
from manually import helpers

df = pd.read_csv(path_final_csv)

choices = helpers.get_choices(df)

answer = questionary.autocomplete(
    "Enter the title you want to remove:",
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
].index

confirmation = input(f"Are you sure you want to remove {clean_title} ({clean_type.lower()}) from your csv?: ")
if confirmation == 'y':
    df = df.drop(new_row)

df.to_csv(path_final_csv, index=False)
