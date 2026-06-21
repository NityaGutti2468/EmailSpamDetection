import streamlit as st
import pickle

model = pickle.load(open("model_email.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer_email.pkl", "rb"))

st.title("Email Spam Detection")

email = st.text_area("Enter Email Text")

if st.button("Predict"):

    transformed_email = vectorizer.transform([email])

    prediction = model.predict(transformed_email)

    if prediction[0] == 1:
        st.error("Spam Email")
    else:
        st.success("Not Spam")