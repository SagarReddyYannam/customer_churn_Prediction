# Customer Churn Prediction

A Machine Learning project that predicts whether a customer is likely to churn (leave the service) based on customer information.

## Project Overview

Customer churn is an important problem for companies. This project uses Machine Learning algorithms to predict customer churn.

The project includes:
- Data exploration and preprocessing
- Feature engineering
- Model training
- Customer churn prediction
- Streamlit web application

## Project Objective

The objective of this project is to predict whether a customer is likely to churn based on their service and account information.

The model can help businesses identify customers who may leave and take suitable actions to retain them.

## Machine Learning Models

The following models were used:

- Logistic Regression
- Random Forest Classifier

The trained models and preprocessing files are saved in the `models` folder.


## Model Performance

The project uses Logistic Regression and Random Forest Classifier.

The models were evaluated using accuracy, precision, recall, and F1-score.

## Future Improvements

- Improve model accuracy through hyperparameter tuning
- Add more machine learning models
- Deploy the application online
- Add visualizations to the Streamlit application

## Project Structure

```text
customer_churn_Prediction/
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── models/
│   ├── feature_columns.pkl
│   ├── logistic_regression_model.pkl
│   ├── random_forest_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── src/
│   └── predict.py
│
├── app.py
├── requirements.txt
└── README.md



## Features

- Predicts whether a customer is likely to churn
- Shows churn probability
- Uses Logistic Regression and Random Forest
- User-friendly Streamlit web application
- Handles customer data preprocessing



## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Jupyter Notebook
- Joblib




## How to Run

1. Create and activate the virtual environment.
2. Install the required packages:

```bash
pip install -r requirements.txt

##Run the Streamlit applications

streamlit run app.py

##Open the URL shown in the terminal

###  Model Output
```markdown
## Model Output

The application provides:

- Churn Prediction: Yes or No
- Churn Probability: Percentage indicating the likelihood of churn



## Dataset

The project uses the Telco Customer Churn dataset.

The dataset contains customer information such as:
- Contract type
- Payment method
- Internet service
- Monthly charges
- Tenure
- Customer churn status



## Conclusion

This project demonstrates an end-to-end Machine Learning workflow for customer churn prediction, including data preprocessing, feature engineering, model training, evaluation, and deployment using Streamlit.

The application allows users to enter customer information and receive a churn prediction along with the churn probability.





