# Project-7-disaster-tweet-classifier-
# 🚨 Disaster Tweet Classifier 🌪️🔥

## 📖 Overview
In today's digital age, social media platforms like Twitter play a crucial role in disseminating information during emergencies. However, distinguishing between tweets that indicate a real disaster (e.g., "Forest fire near La Ronge Sask.") and those that use disaster-related words metaphorically (e.g., "This traffic is a disaster!") can be challenging. 

This project features a Natural Language Processing (NLP) machine learning model that accurately classifies text to determine the true intent behind the language used in tweets.

## 🌐 Live Demo
You can test the AI model live here: **[Paste your Streamlit Cloud URL right here!]**

## 🛠️ Tech Stack
* **Language:** Python
* **Data Processing & ML:** Pandas, Scikit-Learn
* **NLP Techniques:** Regular Expressions (Regex) for text cleaning, TF-IDF (Term Frequency-Inverse Document Frequency) for feature extraction
* **Model:** Logistic Regression
* **Web Framework & Deployment:** Streamlit, Streamlit Community Cloud

## ⚙️ How It Works
1. **Text Cleaning:** The app takes the user's input and strips away URLs, special characters, and punctuation.
2. **Feature Engineering:** The cleaned text is passed through a pre-trained TF-IDF Vectorizer, transforming the English words into a numerical format the AI can understand.
3. **Prediction:** The Logistic Regression model evaluates the numerical vector and outputs a prediction: `1` for a real emergency, or `0` for a non-emergency.

## 🚀 How to Run Locally
If you want to download and run this project on your own machine:

1. Clone this repository to your local computer.
2. Open your terminal and install the required dependencies:
   ```bash
   pip install -r requirements.txt
Run the Streamlit web application:-
   streamlit run app.py
