import streamlit as st
import pickle


# Load model + vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


# Title + Subtitle (Fixed spacing)
st.markdown(
    "<h1 style='text-align: center; margin-bottom: 2px;'>Spam Email Classifier</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; margin-top: 0px; margin-bottom: 0px;'>Enter an email and check if it's spam</p>",
    unsafe_allow_html=True
)

# Input Label (tight spacing)
st.markdown(
    "<p style='font-weight: bold; font-size: 18px; margin-bottom: 5px;'>Paste your email here:</p>",
    unsafe_allow_html=True
)

# Input box
email_input = st.text_area("", height=180)

# Add spacing before button
st.markdown("<div style='margin-top: 5px;'></div>", unsafe_allow_html=True)

# Button
if st.button("Check Email"):

    if email_input.strip() == "":
        st.warning("Please enter an email.")
    else:
        # Transform input
        vector = vectorizer.transform([email_input])

        # Predict
        prediction = model.predict(vector)[0]
        probabilities = model.predict_proba(vector)[0]

        confidence = max(probabilities)

        # Result Output
        if prediction == "spam":
            st.error(f"Spam ({confidence:.2f})")
        else:
            st.success(f"Not Spam ({confidence:.2f})")

        # Confidence Breakdown
        st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
        st.markdown("### Confidence Breakdown")

        labels = model.classes_
        probs = probabilities

        spam_prob = probs[list(labels).index('spam')]
        not_spam_prob = probs[list(labels).index('not spam')]

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"""
            <div style="
                border: 2px solid #ff4b4b;
                border-radius: 12px;
                padding: 20px;
                text-align: center;
                background-color: #fff5f5;
            ">
                <h4>Spam</h4>
                <h2 style="color: #ff4b4b;">{spam_prob:.2f}</h2>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div style="
                border: 2px solid #4CAF50;
                border-radius: 12px;
                padding: 20px;
                text-align: center;
                background-color: #f6fff6;
            ">
                <h4>Not Spam</h4>
                <h2 style="color: #4CAF50;">{not_spam_prob:.2f}</h2>
            </div>
            """, unsafe_allow_html=True)