import streamlit as st
import pickle

# Load saved models
with open("models/classifier.pkl", "rb") as f:
    clf = pickle.load(f)

with open("models/regressor.pkl", "rb") as f:
    reg = pickle.load(f)

with open("models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

st.set_page_config(page_title="AutoJudge", layout="centered")

st.title("🧠 AutoJudge")
st.subheader("Programming Problem Difficulty Predictor")

st.markdown("Paste the problem details below:")

title = st.text_input("Problem Title")
desc = st.text_area("Problem Description", height=150)
inp = st.text_area("Input Description", height=100)
out = st.text_area("Output Description", height=100)

if st.button("Predict Difficulty"):
    if desc.strip() == "":
        st.warning("Please enter at least the problem description.")
    else:
        full_text = title + " " + desc + " " + inp + " " + out
        X = vectorizer.transform([full_text])

        pred_class = clf.predict(X)[0]
        pred_score = reg.predict(X)[0]

        st.success(f"📌 Predicted Difficulty Class: **{pred_class}**")
        st.success(f"📊 Predicted Difficulty Score: **{round(pred_score, 2)}**")
