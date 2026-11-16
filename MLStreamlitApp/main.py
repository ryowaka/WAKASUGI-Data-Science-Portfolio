import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.title("Machine Learning Streamlit App")
st.write("This app allows users to train and evaluate machine learning models.")

df = pd.read_csv("MLStreamlitApp/data/pokemon_alopez247.csv")
st.subheader("Dataset Preview")
st.dataframe(df)
