import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.title("Machine Learning Streamlit App")
st.write("This app allows users to train and evaluate machine learning models.")


data_selection = st.selectbox(
    "Choose a dataset",
    ["Pokemon Dataset", "Upload CSV"]
)

if data_selection == "Pokemon Dataset":
    df = pd.read_csv("MLStreamlitApp/data/pokemon_alopez247.csv")

    st.subheader("Dataset Preview")
    st.dataframe(df)

else:
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader("Uploaded Dataset Preview")
        st.dataframe(df)
    else:
        st.warning("Please upload a CSV file to proceed.")