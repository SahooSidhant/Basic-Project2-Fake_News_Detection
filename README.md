
📌 Fake News Detection Using Machine Learning
📰 Overview

This project is a Fake News Detection Web App built using Machine Learning (Linear SVM + TF-IDF) and deployed using Streamlit.
It classifies news articles as REAL or FAKE based on textual patterns



🚀 Live Demo

👉 (Add your Streamlit link here after deployment)




📸 Screenshots
🟢 Real News Prediction
<img width="1918" height="966" alt="Screenshot 2026-06-18 133607" src="https://github.com/user-attachments/assets/63c10528-6b64-4e2b-a240-5ca51fba4d41" />




🔴 Fake News Prediction




🧠 How It Works
        1. Input news article text
        2. Text is cleaned and preprocessed
        3. TF-IDF vectorization converts text into numerical features
        4. Linear SVM model predicts:
            ---REAL
            ---FAKE


⚙️ Tech Stack
        Python 🐍
        Streamlit 🎈
        Scikit-learn 🤖
        Pandas & NumPy 📊
        Joblib 🧩
        NLP (TF-IDF)



📂 Project Structure

Fake-News-Detection/
├── data
│   ├── Fake.csv
│   └── Teal.csv
├── app.py
├── models/
│   ├── linear_svm_model.pkl
│   └── tfidf_vectorizer.pkl
├── background.jpg
├── requirements.txt
└── README.md


📊 Model Details
Algorithm: Linear Support Vector Machine (SVM)
Feature Extraction: TF-IDF (with unigrams + bigrams)
Preprocessing: Lowercasing, stopword removal, noise cleaning
Output: Binary classification (FAKE / REAL)




🎯 Features
Real-time prediction
Clean UI with Streamlit
Dark-themed newspaper design
Instant analysis of news text
Simple and fast ML pipeline




📈 Future Improvements
Add deep learning (BERT model)
Show confidence score (%)
Highlight fake words in text
Multi-language support




👨‍💻 Author

Sidhanta Sahoo


📜 License

This project is open-source and free to use.
