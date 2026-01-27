import pandas as pd

# get a df a return a list with all the native titles and english titles plus its type
def get_choices(df):
    choices = []
    for _, row in df.iterrows():
        t_type = f" ({row['type']})"
        
        # Add native title with type
        if pd.notna(row['title']):
            choices.append(f"{row['title']}{t_type}")
            
        # Add english title with type (if it exists)
        if pd.notna(row['english_title']):
            choices.append(f"{row['english_title']}{t_type}")

    return choices

def get_title_type(answer):
    # Extract both parts from: "Adachi to Shimamura (tv)"
    try:
        clean_title = answer.rsplit(' (', 1)[0]
        clean_type = answer.rsplit(' (', 1)[1].rstrip(')')
    except Exception:
        return 1, 1

    return clean_title, clean_type

def sort_final(df, sort_final):
    if sort_final.get("date"):
        df = df.sort_values(by="start_date")
    elif sort_final.get("title"):
        df = df.sort_values(by="title")

    return df
