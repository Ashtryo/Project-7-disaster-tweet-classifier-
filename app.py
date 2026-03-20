import streamlit as st
import pickle
import re

# 1. Page Configuration (Must be the very first Streamlit command)
st.set_page_config(
    page_title="Disaster AI",
    page_icon="🚨",
    layout="centered"
)

# 2. Add Custom CSS for Colors and Styling
st.markdown("""
<style>
    /* Change the background color */
    .stApp {
        background-color: #f0f8ff;
    }
    /* Style the main title */
    .main-title {
        color: #ff4b4b;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px #cccccc;
        margin-bottom: 10px;
    }
    /* Style the subtitle */
    .sub-title {
        color: #4f4f4f;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# 3. Load the AI and Translator
@st.cache_resource
def load_models():
    model = pickle.load(open('disaster_model.pkl', 'rb'))
    vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
    return model, vectorizer

model, vectorizer = load_models()

# 4. Define the cleaning function
def clean_text(text):
    text = re.sub(r'http\S+', '', str(text))  # Remove URLs
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)  # Remove special characters
    return text.lower()  # Convert to lowercase

# 5. Beautiful UI Headers
st.markdown('<div class="main-title">🚨 Disaster Tweet Classifier 🌪️🔥</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Paste a tweet below and let our AI brain determine if it is a real emergency! 🧠✨</div>', unsafe_allow_html=True)

# 6. User Input Area
user_tweet = st.text_area("✍️ Enter the tweet here:", height=120, placeholder="Type or paste a tweet here...")

# 7. Create columns to center the button nicely
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_button = st.button("🔍 Analyze Tweet", use_container_width=True)

# 8. Prediction Logic with Animations
if predict_button:
    if user_tweet.strip() == "":
        st.warning("⚠️ Please enter a tweet first before checking!")
    else:
        # Add a cool loading spinner while the AI "thinks"
        with st.spinner("🤖 AI is analyzing the text..."):
            cleaned = clean_text(user_tweet)
            tweet_vector = vectorizer.transform([cleaned])
            prediction = model.predict(tweet_vector)
        
        st.markdown("---")
        
        # Display big, colorful results
        if prediction[0] == 1:
            st.error("### 🚨 DANGER!\n**The AI predicts this is a REAL disaster tweet.**")
        else:
            st.success("### ✅ SAFE!\n**The AI predicts this is NOT a real disaster.** Just normal conversation.")
            st.balloons()  # Fun animation for safe tweets!