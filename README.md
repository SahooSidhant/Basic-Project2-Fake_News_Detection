
<h1>📌 **Fake News Detection Using Machine Learning**</h1>


<h2>📰 Overview</h2>

The Fake News Detection System is a machine learning web app that classifies news articles as REAL or FAKE using NLP techniques. It uses a TF-IDF vectorizer for feature extraction and a Linear SVM model for classification. The model is trained on labeled news data and deployed using Streamlit for real-time user interaction.

The project demonstrates end-to-end implementation of text preprocessing, feature engineering, model training, and deployment in a simple and interactive UI.

<br><br/>

<h1>🚀 **Live Demo**</h1>


👉 https://fakenewsdetectionbysidhant.streamlit.app/

<br><br/>


<h1>📸 **Screenshots**</h1>


<h2>🟢 Real News Prediction</h2>

<img width="1918" height="966" alt="Screenshot 2026-06-18 133607" src="https://github.com/user-attachments/assets/63c10528-6b64-4e2b-a240-5ca51fba4d41" />




<h2>🔴 Fake News Prediction</h2>


<img width="1917" height="966" alt="Screenshot 2026-06-18 141928" src="https://github.com/user-attachments/assets/d21ba11e-13f8-4fec-8035-4c8d1bf3f694" />

<br><br/>

<h1>🧠 **How It Works**</h1>

        1. Input news article text
        2. Text is cleaned and preprocessed
        3. TF-IDF vectorization converts text into numerical features
        4. Linear SVM model predicts:
            ---REAL
            ---FAKE
<br><br/>

<h1>⚙️ **Tech Stack**</h1>

        * Python 🐍
        * Streamlit 🎈
        * Scikit-learn 🤖
        * Pandas & NumPy 📊
        * Joblib 🧩
        * NLP (TF-IDF)

<br><br/>

<h1>📂 **Project Structure**</h1>

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

<br><br/>
<h1>📊 **Model Details**</h1>

        - Algorithm: Linear Support Vector Machine (SVM)
        - Feature Extraction: TF-IDF (with unigrams + bigrams)
        - Preprocessing: Lowercasing, stopword removal, noise cleaning
        - Output: Binary classification (FAKE / REAL)


<br><br/>

<h1>🎯 **Features**</h1>

        - Real-time prediction
        - Clean UI with Streamlit
        - Dark-themed newspaper design
        - Instant analysis of news text
        - Simple and fast ML pipeline



<br><br/>
<h1>📈 **Future Improvements**</h1>
        
        * Add deep learning (BERT model)
        * Show confidence score (%)
        * Highlight fake words in text
        * Multi-language support



<br><br/>
<h2>👨‍💻 Author</h2>

<h3>Sidhanta Sahoo</h3>

<br><br/>
<h2>📜 License</h2>

<h3>This project is open-source and free to use.</h3>
