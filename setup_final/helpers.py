from datetime import datetime

valid_type = ["tv", "ona", "ova", "movie"]
SEASONS = ["winter", "spring", "summer", "fall"]

def keep_season_only(df, column_name):
    # Split the string in column_name and only the first string is keep.

    df[column_name] = df[column_name].str.split().str[0]
    return df

# if the current month is bigger than 10, then we are in the last season of the year and i don't care about shutting out any anime
# from this year, only about the next year.
# In the opposite case, depending of the month I shutout the yet to come season.
# as you can see in the first inner if, if we are in the first season then it shuout sping, summer and fall
def filter_season(df):
    now = datetime.now()
    current_month, current_year = now.month, now.year

    if current_month < 10:

        if current_month >= 1 and current_month < 4:
            del SEASONS[0]
        elif current_month >= 4 and current_month < 7:
            del SEASONS[0:2]
        elif current_month >= 7 and current_month < 10:
            del SEASONS[0:3]

        df = df[~((df["season"].str.lower().isin(SEASONS) & (df["start_date"].dt.year == current_year)))]
    else:
        df = df[~(df["start_date"].dt.year == current_year + 1)]

    return df
    

def filter_type(df, column_name):
    df = df[df[column_name].str.lower().isin(valid_type)]
    return df

def sort_final(df, sort_final):
    if sort_final.get("date"):
        df = df.sort_values(by="start_date")
    elif sort_final.get("title"):
        df = df.sort_values(by="title")

    return df



