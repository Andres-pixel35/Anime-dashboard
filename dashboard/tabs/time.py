import pandas as pd
import streamlit as st

def render_time(df):
    # tab's title
    st.markdown("<h1 style='text-align: center;'>Time</h1>", unsafe_allow_html=True)
 
    # get amount of time in minutes watching anime
    time = df["complete_duration"].sum()
    time = int(round(time / 60, 0)) # time in hours

    st.metric(label="Watching anime (hours)", value=time)
    
    # get the amount of anime per each year
    df["start_date"] = pd.to_datetime(df["start_date"])
    years = df["start_date"].dt.year.value_counts().sort_index()

    # get older anime
    df["start_date"] = df["start_date"].dt.date
    old = df.loc[:, ["title", "english_title", "start_date"]]    
    old = old.sort_values(by="start_date")
    top5 = old.iloc[0:5]

    # get seasons distribution
    season = df.groupby("season")["season"].value_counts()
    season = round((season / len(df)) * 100, 2)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Seasonal Share")
        st.dataframe(season, width="stretch")

    with col2:
        st.markdown("### Older Works")
        st.dataframe(top5, hide_index=True, width="stretch")
    
    st.markdown("#### Release year distribution")
    st.bar_chart(years, y_label="Frequency", x_label="Year")






