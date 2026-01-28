import streamlit as st

def render_watched(df):
    # tab title
    st.markdown("<h1 style='text-align: center;'>Watched</h1>", unsafe_allow_html=True)

    # get total of episodes watched
    episodes = int(df["episodes"].sum())

    st.metric(label="Episodes", value=episodes)

    # get the longest and shortest works by episodes
    filter_episodes = df.loc[:, ["title", "english_title", "episodes"]]

    filter_episodes = filter_episodes.dropna(subset="episodes")
    filter_episodes = filter_episodes.sort_values(by="episodes")

    shortest = filter_episodes.iloc[0:5]
    longest = filter_episodes.iloc[:-6:-1]

    # get genres and tags
    df["genres"] = df["genres"].str.split(";")
    df["tags"] = df["tags"].str.split(";")

    genres = df.explode("genres")["genres"].value_counts().sort_values(ascending=False)
    tags = df.explode("tags")["tags"].value_counts().sort_values(ascending=False)

    # get source distribution
    source = df.groupby("source")["source"].value_counts().sort_values(ascending=False)
    source = source / len(df) * 100
    source = round(source,2)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Shortest Works")
        st.dataframe(shortest, hide_index=True, width="stretch")

    with col2: 
        st.markdown("### Longest Works")
        st.dataframe(longest, hide_index=True, width="stretch")

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("### Genres")
        st.dataframe(genres, height=210, width="stretch")

    with col4:
        st.markdown("### Tags")
        st.dataframe(tags, height=210, width="stretch")

    st.markdown("#### Source Share")
    st.dataframe(source, height=210, width="stretch")
