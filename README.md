# 🐦 Twitter Sentiment Analysis using Representation Learning

This project is an **Unsupervised Machine Learning based Sentiment Analysis application** that uses **Representation Learning** techniques to understand and classify the sentiment of tweets as **Positive, Neutral, or Negative**.

The application is built using **Streamlit** and **Hugging Face Transformers** and demonstrates how modern NLP models learn meaningful text representations automatically.

---

## 🔗 Live Demo

👉 **Click Here:** https://sentiment-analysis-app-gk3mqvnxymqtpl9yijb7ef.streamlit.app/

---

## 📌 Problem Statement

Computers cannot directly understand human language.  
To analyze opinions expressed in tweets, text must be converted into meaningful numerical representations.

The goal of this project is to:
- Convert raw tweet text into numerical representations
- Use representation learning to capture semantic meaning
- Classify sentiment accurately without manual feature engineering

---

## 🧠 Representation Learning Overview

**Representation Learning** is a machine learning technique where models automatically learn useful features from raw data instead of relying on manually engineered features.

In Natural Language Processing:
- Words and sentences are converted into **dense vector representations**
- Similar words have similar vector values
- Context and meaning are captured effectively

This project uses **pre-trained transformer-based representations** to perform sentiment analysis.

---

## 📖 What is Sentiment Analysis?

Sentiment Analysis is the process of identifying the emotional tone of text and classifying it into:
- **Positive**
- **Neutral**
- **Negative**

It helps in understanding opinions, emotions, and attitudes expressed in written language, especially on social media platforms like Twitter.

---

## ⚙️ How the System Works

1. **Input Text**  
   A tweet entered by the user

2. **Text Processing**  
   The text is tokenized and prepared by the transformer model

3. **Representation Learning**  
   A pre-trained transformer converts text into contextual embeddings

4. **Sentiment Classification**  
   The model predicts sentiment based on learned representations

5. **Output**  
   Sentiment label with confidence score and visualization

---

## 🧠 Model Used

- **Model Name:** `cardiffnlp/twitter-roberta-base-sentiment-latest`
- **Architecture:** Transformer (RoBERTa-based)
- **Training:** Pre-trained on large-scale Twitter data
- **Classes:** Positive, Neutral, Negative
- **Approach:** Unsupervised (no custom dataset training)

---

## ✨ Features of the Application

- 📊 Demo tweet sentiment analysis
- ✍️ Custom tweet sentiment analysis
- 😊 Three-class sentiment classification
- 📈 Interactive sentiment distribution pie chart
- 📋 Confidence score for predictions
- ⚡ Fast and user-friendly Streamlit interface

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Hugging Face Transformers**
- **PyTorch**
- **Pandas**
- **Plotly**


---
