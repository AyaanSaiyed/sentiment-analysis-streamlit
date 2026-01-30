import streamlit as st
from transformers import pipeline
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="Twitter Sentiment Analysis", page_icon="🐦", layout="wide")

# --- TITLE ---
st.title("🐦 Twitter Sentiment Analysis Dashboard")
st.write("Analyze tweets and visualize sentiment")

# --- LOAD MODEL ONCE ---
if "analyzer" not in st.session_state:
    with st.spinner("Loading sentiment model..."):
        # Use a 3-class model (Positive, Neutral, Negative)
        st.session_state.analyzer = pipeline(
            "sentiment-analysis",
            model="cardiffnlp/twitter-roberta-base-sentiment-latest"
        )

# --- MODE SELECTION ---
mode = st.radio("Select Mode:", ["Demo Tweets", "Custom Tweet"])

# --- SENTIMENT FUNCTION ---
def analyze_sentiment(text):
    result = st.session_state.analyzer(text)[0]
    label_map = {
        "LABEL_0": "NEGATIVE",
        "LABEL_1": "NEUTRAL",
        "LABEL_2": "POSITIVE",
        "POSITIVE": "POSITIVE",
        "NEGATIVE": "NEGATIVE",
        "NEUTRAL": "NEUTRAL"
    }
    sentiment = label_map.get(result["label"].upper(), result["label"])
    confidence = result["score"] * 100
    return sentiment, confidence

# --- DEMO DATA ---
demo_tweets = [
    "Just tried the new iPhone! Amazing camera quality!",          # Positive
    "Terrible customer service. Waited 2 hours!",                 # Negative
    "The new update is okay, nothing special.",                   # Neutral
    "Battery life seems fine so far.",                            # Neutral
    "Best purchase ever! Highly recommend!",                      # Positive
    "Worst product I’ve ever bought. Waste of money.",             # Negative
    "The phone was delivered on time as expected.",                # Neutral
    "Overall performance is decent, not great, not bad.",          # Neutral
    "Customer support was helpful and polite.",                    # Positive
    "Delivery got delayed again, pretty annoying."                 # Negative
]

# --- MAIN LOGIC ---
if mode == "Demo Tweets":
    st.subheader("📊 Demo Tweet Sentiment Analysis")
    data = []
    for i, text in enumerate(demo_tweets, start=1):
        sentiment, confidence = analyze_sentiment(text)
        data.append({
            "Tweet_ID": i,
            "Tweet": text,
            "Sentiment": sentiment,
            "Confidence (%)": round(confidence, 2)
        })

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    # Visualization
    fig = px.pie(
        df,
        names="Sentiment",
        title="Sentiment Distribution",
        color="Sentiment",
        color_discrete_map={"POSITIVE": "green", "NEGATIVE": "red", "NEUTRAL": "gray"}
    )
    st.plotly_chart(fig, use_container_width=True)

elif mode == "Custom Tweet":
    st.subheader("✍️ Analyze a Custom Tweet")
    text = st.text_area("Enter a tweet:", placeholder="Type or paste a tweet here...")
    if st.button("Analyze"):
        if text.strip():
            sentiment, confidence = analyze_sentiment(text)
            st.success(f"**Sentiment:** {sentiment} ({confidence:.1f}% confidence)")
        else:
            st.warning("Please enter some text.")

# streamlit run sentiment.py