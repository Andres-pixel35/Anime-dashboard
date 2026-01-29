import pandas as pd
import streamlit as st
from config import path_final_csv, user_name 
from tabs import time, score, watched, summarize

df = pd.read_csv(path_final_csv)

st.set_page_config(layout="wide")

with st.sidebar:
    st.header("FIlter type")
    choices = st.multiselect("Pick types:", df['type'].unique())

    st.info("You may choose more than one option")

if choices:
    df = df[df['type'].isin(choices)]

st.title(f"{user_name}'s Anime Dashboard")

#  tabs names
tab1, tab2, tab3, tab4 = st.tabs(["Summarize", "Watched", "Time", "Score"])

# Content for Tab 1
with tab1:
    summarize.render_summarize(df)

# Content for Tab 2
with tab2:
    watched.render_watched(df)

# Content for Tab 3
with tab3:
    time.render_time(df)

# Content for Tab 4
with tab4:
    score.render_score(df)




