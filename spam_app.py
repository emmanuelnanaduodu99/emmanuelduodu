import streamlit as st # type: ignore
import pickle

# Load the trained model and vectorizer
with open('spam_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    loaded_vectorizer = pickle.load(vectorizer_file)

# App title and description
st.title("MailGuard: Keep Your Mail Safe")
st.write("Welcome to the Spam Email Classifier! This app will help you identify whether an email is *Spam* or *Ham* (non-spam).")

# User input for email content
email_input = st.text_area("Enter the email content for classification:")

# Button to trigger classification
if st.button("Classify"):
    if email_input:
        # Transform the input text to the format the model understands
        vect = loaded_vectorizer.transform([email_input]).toarray()
        
        # Predict the classification (Spam or Ham)
        prediction = loaded_model.predict(vect)
        
        # Display the classification result
        result = "Spam" if prediction[0] == 1 else "Ham"
        st.write(f"**Prediction Result:** This email is classified as: **{result}**")
    else:
        st.write("Please enter the email content for classification.")