import streamlit as st
import pickle

# Page Config
st.set_page_config(
    page_title="Email Spam Detector",
    page_icon="📧",
    layout="wide"
)

# Load Model
model = pickle.load(open("model_email.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer_email.pkl", "rb"))

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.title {
    text-align: center;
    color: #1E88E5;
    font-size: 40px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: gray;
    font-size: 18px;
}
.result-box {
    padding: 15px;
    border-radius: 10px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="title">📧 Email Spam Detection System</p>',
            unsafe_allow_html=True)

st.markdown(
    '<p class="subtitle">Detect whether an email is Spam or Ham using Machine Learning</p>',
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    st.header("ℹ️ About")
    st.write("""
    This application uses a trained Machine Learning model to classify emails as:
    
    ✅ Not Spam
    
    🚨 Spam
    """)
    st.info("Built using Streamlit & Scikit-Learn")

# Main Layout
col1, col2 = st.columns([3, 1])

with col1:
    email = st.text_area(
        "✉️ Enter Email Text",
        height=250,
        placeholder="Paste your email content here..."
    )

with col2:
    st.metric("Model", "ML Classifier")
    st.metric("Status", "Ready")

# Prediction
if st.button("🔍 Analyze Email", use_container_width=True):

    if email.strip() == "":
        st.warning("Please enter email content.")
    else:
        transformed_email = vectorizer.transform([email])

        prediction = model.predict(transformed_email)

        # Probability (if model supports it)
        try:
            prob = model.predict_proba(transformed_email)
            confidence = max(prob[0]) * 100
        except:
            confidence = None

        st.divider()

        if prediction[0] == 1:
            st.error("🚨 This Email is SPAM")

            if confidence:
                st.progress(int(confidence))
                st.write(f"Confidence: **{confidence:.2f}%**")

        else:
            st.success("✅ This Email is NOT SPAM")

            if confidence:
                st.progress(int(confidence))
                st.write(f"Confidence: **{confidence:.2f}%**")

# Footer
st.markdown("---")
st.caption("Developed by Nitya Gutti")
