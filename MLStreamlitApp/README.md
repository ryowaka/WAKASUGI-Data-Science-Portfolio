# Machine Learning Streamlit App


## Overview

I created a Streamlit app where users can train and evaluate machine learning models. They can use the sample dataset or upload their own CSV file, select a target, choose a model, and change its hyperparameters.


## Streamlit App

App link:


## Dataset

[Mobile Price Classification Dataset (Kaggle)](https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification)

This dataset contains information about mobile phones, such as RAM, battery power, and screen size. I chose `price_range` as the default target because I wanted to predict the price category of a mobile phone based on its specifications.

Users can also choose a different target.


## How to Run Locally

1. Clone this repository.
2. Open the repository folder in VS Code.
3. Install the libraries:
   `pip install -r MLStreamlitApp/requirements.txt`
4. Run the app:
   `streamlit run MLStreamlitApp/main.py`


## Libraries

- pandas (3.0.5)
- seaborn (0.13.2)
- matplotlib (3.11.1)
- streamlit (1.63.0)
- scikit-learn (1.9.1)


## Machine Learning Models

I used two models that we learned in class:

- **KNN:** Users can change the number of neighbors.
- **Decision Tree:** Users can change the maximum depth and minimum samples split.

I used 80% of the data for training and 20% for testing. I also used StandardScaler for KNN.

Users can compare the results using accuracy, precision, recall, F1-score, and a confusion matrix.


## References

- [Streamlit Cheat-Sheet](https://cheat-sheet.streamlit.app/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
