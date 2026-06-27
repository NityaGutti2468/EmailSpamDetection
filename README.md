# 📧 Email Spam Detection  

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)  
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikit-learn)](https://scikit-learn.org/stable/)  
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-brightgreen?style=for-the-badge&logo=streamlit)](https://emailspamdetection-8tweedhgll6xevycyfhxy6.streamlit.app/)  

A **Machine Learning + NLP** project to classify emails as **Spam** or **Not Spam**, deployed with **Streamlit Cloud**.  

---

## 🚀 Project Overview  
Spam emails are unsolicited, fraudulent, or irrelevant messages sent in bulk.  
This project leverages **Natural Language Processing (NLP)** and **Machine Learning** to automatically detect and filter spam emails, ensuring a safer and cleaner inbox.  

---

## 🛠️ Tech Stack  
- **Python** 🐍  
- **Streamlit** 🎨 (for interactive UI)  
- **Scikit-learn** 🤖 (ML algorithms)  
- **Pandas & NumPy** 📊 (data handling)  
- **TF-IDF Vectorizer** ✍️ (text feature extraction)  
- **Pickle** 📦 (model persistence)  

---

## 📂 Project Files

- `app.py` → Streamlit application
- `model_email.pkl` → Trained machine learning model
- `vectorizer_email.pkl` → TF-IDF vectorizer
- `README.md` → Project documentation

---

## ⚙️ Features  
✅ Real-time spam detection  
✅ Clean and simple Streamlit interface  
✅ TF-IDF text vectorization for feature extraction  
✅ Lightweight and fast predictions  

---

## 📊 Workflow  

1. **Data Collection**  
2. **Text Preprocessing** (cleaning, tokenization, stopword removal)  
3. **Feature Extraction** (TF-IDF vectorization)  
4. **Model Training** (Naive Bayes, Logistic Regression, etc.)  
5. **Model Serialization** (Pickle for saving model & vectorizer)  
6. **Deployment** (Streamlit Cloud)  

---

## ▶️ Run Locally  


# Step 1: Clone Repository
git clone https://github.com/NityaGutti2468/EmailSpamDetection.git

# Step 2: Install Dependencies
pip install -r requirements.txt

# Step 3: Launch Streamlit App
streamlit run app.py

---
### 🧠 Sample Prediction
Email Text	                        |  Prediction |
Congratulations! You won a lottery	|  Spam  |
Meeting scheduled at 5 PM	          |  Not Spam

-----
## 🌐 Live Demo

Check out the deployed Streamlit app here:

🔗 [Email Spam Detection App](https://emailspamdetection-8tweedhgll6xevycyfhxy6.streamlit.app/)
-----
## 🚀 Deployment

This project is deployed using **Streamlit Cloud**.
-------------
### 📌 Future Improvements
- Deep Learning based prediction
- Better text preprocessing
- Email API integration
----------
### 👩‍💻 Author

Nitya Gutti
