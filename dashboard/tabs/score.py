import streamlit as st

def render_score(df):

    st.markdown("<h1 style='text-align: center;'>Score</h1>", unsafe_allow_html=True)

    # get score mean
    score_mean = int(round(df["score"].mean(), 0))

    st.metric(label="Mean", value=score_mean)

    # get worst and best scored works
    score = df.loc[:, ["title", "english_title", "score"]]
    score = score.sort_values(by="score")

    worst = score.iloc[0:5]
    best = score[:-6:-1]

    # get score distribution
    score_distribution = df.groupby("score")["score"].value_counts().sort_index()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Five worst ranked works")
        st.dataframe(worst, hide_index=True, width="stretch")

    with col2:
        st.markdown("### Five best ranked works")
        st.dataframe(best, hide_index=True, width="stretch")

    st.markdown("#### Score distribution")
    st.bar_chart(score_distribution, x_label="Score", y_label="Frequency")

