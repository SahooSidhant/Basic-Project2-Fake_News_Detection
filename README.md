
📌 <h1>**Fake News Detection Using Machine Learning**</h1>


📰 <h2>**Overview**</h2>

The Fake News Detection System is a machine learning web app that classifies news articles as REAL or FAKE using NLP techniques. It uses a TF-IDF vectorizer for feature extraction and a Linear SVM model for classification. The model is trained on labeled news data and deployed using Streamlit for real-time user interaction.

The project demonstrates end-to-end implementation of text preprocessing, feature engineering, model training, and deployment in a simple and interactive UI.



🚀 <h1>**Live Demo**</h1>


👉 https://fakenewsdetectionbysidhant.streamlit.app/




📸 **Screenshots**


🟢 Real News Prediction

<img width="1918" height="966" alt="Screenshot 2026-06-18 133607" src="https://github.com/user-attachments/assets/63c10528-6b64-4e2b-a240-5ca51fba4d41" />




🔴 Fake News Prediction


<img width="1917" height="966" alt="Screenshot 2026-06-18 141928" src="https://github.com/user-attachments/assets/d21ba11e-13f8-4fec-8035-4c8d1bf3f694" />



🧠 **How It Works**

        1. Input news article text
        2. Text is cleaned and preprocessed
        3. TF-IDF vectorization converts text into numerical features
        4. Linear SVM model predicts:
            ---REAL
            ---FAKE


⚙️ **Tech Stack**

        Python 🐍
        Streamlit 🎈
        Scikit-learn 🤖
        Pandas & NumPy 📊
        Joblib 🧩
        NLP (TF-IDF)



📂 **Project Structure**

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


📊 **Model Details**

        Algorithm: Linear Support Vector Machine (SVM)
        Feature Extraction: TF-IDF (with unigrams + bigrams)
        Preprocessing: Lowercasing, stopword removal, noise cleaning
        Output: Binary classification (FAKE / REAL)




🎯 **Features**

        Real-time prediction
        Clean UI with Streamlit
        Dark-themed newspaper design
        Instant analysis of news text
        Simple and fast ML pipeline




📈 **Future Improvements**
        
        Add deep learning (BERT model)
        Show confidence score (%)
        Highlight fake words in text
        Multi-language support




👨‍💻 Author

Sidhanta Sahoo


📜 License

This project is open-source and free to use.
