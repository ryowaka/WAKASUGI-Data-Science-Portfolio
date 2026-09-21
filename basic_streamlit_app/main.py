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

# Read the Palmer's Penguins dataset from a CSV file.
df = pd.read_csv("data/penguins.csv")

# Display Summary Statistics
st.subheader("**Summary Statistics**")
st.dataframe(df.describe())

# DIsplay the scatterplot of flipper length and body mass, colored by species
st.subheader("**Flipper Length and Body Mass Relationship by Species**")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="flipper_length_mm", y="body_mass_g", hue="species", ax=ax)
st.pyplot(fig)

# Display a boxplot comparing the distributions of a selected feature across species
feature = st.selectbox("**Choose a feature to compare**", 
                       ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"])

st.subheader(f"**{feature} by Species**")
fig, ax = plt.subplots()
sns.boxplot(data=df, x=feature, y="species", ax=ax)
st.pyplot(fig)

# Display a dataframe of the selected species
species = st.selectbox("**Choose a species to explore**",
                       df["species"].dropna().unique())
species_data = df[df["species"] == species]
st.subheader(f"**Data for {species}**")
st.dataframe(species_data)


