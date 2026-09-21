import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.title("Palmer's Penguins Dataset Exploration")
st.markdown("""
This app explores:
- **Data Validation:** Checking data types, data characteristics, and basic consistency.
- **Visualization:** Using scatterplots and boxplots to compare the physical characteristics of different penguin species.
""")

if st.button("Send balloons!"):
    st.balloons()

df = pd.read_csv("data/penguins.csv")

st.write("**Summary Statistics**")
st.dataframe(df.describe())

st.write("**Flipper Length and Body Mass Relationship by Species**")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="flipper_length_mm", y="body_mass_g", hue="species", ax=ax)
st.pyplot(fig)

feature = st.selectbox("Choose a feature to compare", 
                       ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"])

st.write(f"**{feature} by Species**")
fig, ax = plt.subplots()
sns.boxplot(data=df, x=feature, y="species", ax=ax)
st.pyplot(fig)

species = st.selectbox("Choose a species to explore",
                       df["species"].unique())
species_data = df[df["species"] == species]
st.write(f"**Data for {species}**")
st.dataframe(species_data)
