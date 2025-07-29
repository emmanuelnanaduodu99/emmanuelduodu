# MailGuard: Spam Mail Detection System

**MailGuard** is a simple and efficient Streamlit-based web app that helps you detect whether an email is **Spam** or **Ham** (non-spam) using Machine Learning.

## 🚀 Features

- 🧠 Machine Learning model (Naive Bayes / Logistic Regression)
- 📨 Classifies emails as Spam or Ham
- 🧾 Clean and simple user interface using Streamlit
- 🎯 Real-time predictions
- 🔒 Easy to use and fast

## 📦 Requirements

- Python 3.8+
- streamlit
- scikit-learn
- pickle (for loading model and vectorizer)

## 🛠️ Installation

1. Clone this repo or download the files.
2. Install required packages:
   ```bash
   pip install streamlit scikit-learn
   
Make sure spam_model.pkl and vectorizer.pkl are in the same folder.

💡 Usage
Run the Streamlit app using the command:

    streamlit run app.py

Then open the provided localhost link in your browser.

🖥️ Interface
Paste or type the content of the email.

Click "Classify".

Get instant result: Spam or Ham.

📁 Files
app.py → Main Streamlit app

spam_model.pkl → Trained ML model

vectorizer.pkl → TF-IDF vectorizer

📌 Note
This is a basic prototype for learning purposes.

Make sure your .pkl files are properly generated using the same preprocessing logic.

✨ Developed by Emmanuel Duodu


