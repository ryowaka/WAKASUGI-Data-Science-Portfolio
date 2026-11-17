import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

st.title("Machine Learning Streamlit App")
st.write("This app allows users to train and evaluate machine learning models.")

data_selection = st.selectbox(
    "Choose a dataset",
    ["Mobile Price Dataset", "Upload CSV file"]
)

if data_selection == "Mobile Price Dataset":
    df = pd.read_csv("MLStreamlitApp/data/mobile_price.csv")

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
        st.stop()




st.subheader("Target Selection")
target = st.selectbox("Select the target column", df.columns)
st.write("You selected", target)

X = df.drop(columns=[target])
y = df[target]

X = X.select_dtypes(include=["number"])

clean_data = pd.concat([X, y], axis=1).dropna()

X = clean_data.drop(columns=[target])
y = clean_data[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)



st.subheader("Model Selection")

model_selection = st.selectbox(
    "Choose a model",
    ["K-Nearest Neighbors", "Decision Tree"]
)

if model_selection == "K-Nearest Neighbors":

    k = st.slider("Numebers of Neighbors:", 1, 20, 5)
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
else:

    max_depth = st.slider("Max depth", 1, 20, 4)
    min_samples_split = st.slider("Min samples split", 2, 20, 2)
    model = DecisionTreeClassifier(
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        random_state=42
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)




st.subheader("Model Evaluation")
accuracy = accuracy_score(y_test, y_pred)

st.write("Accuracy measures the proportion of predictions that are correct")
st.write("**Accuracy**:", accuracy)




st.subheader("Classification Report")

st.write("Precision: The proportion of predictions for a class that are correct.")
st.write("Recall: The proportion of actual members of a class that are correctly identified.")
st.write("F1-score: A measure that balances precision and recall.")
st.write("Support: The number of actual observations in each class.")

st.text(classification_report(y_test, y_pred))



st.subheader("Confusion Matrix")

cm = confusion_matrix(y_test, y_pred)
fig = plt.figure()
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
st.pyplot(fig)

st.write("The confusion matrix shows how many predictions are correct or incorrect for each class." \
"The diagonal elements represent correct predictions, while off-diagonal elements represent misclassifications.")



st.subheader("Target Selection")
