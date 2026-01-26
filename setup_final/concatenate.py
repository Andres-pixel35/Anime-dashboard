import pandas as pd
from config import path_historical_csv, path_modified_airing

pd.set_option("display.max_rows", None)

df1 = pd.read_csv(path_historical_csv)
df2 = pd.read_csv(path_modified_airing)
df_combined = pd.concat([df1, df2], ignore_index=True)

# I keep the information from df2 because is the one with the most update information
df = df_combined.drop_duplicates(subset=["title", "type"], keep="last")
df.loc[:,"start_date"] = pd.to_datetime(df["start_date"]).dt.date
df = df.sort_values(by="start_date")

df.to_csv(path_historical_csv, index=False)
