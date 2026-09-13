import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Load the saved Logistic Regression model
model = joblib.load(
    BASE_DIR / "models" / "logistic_regression_model.pkl"
)

# Load the saved scaler
scaler = joblib.load(
    BASE_DIR / "models" / "scaler.pkl"
)

# Load the feature columns
feature_columns = joblib.load(
    BASE_DIR / "models" / "feature_columns.pkl"
)
def predict_churn(customer_data):
    """
    Predict whether a customer will churn or not.
    """

    # Arrange columns in the same order used during training
    customer_data = customer_data[feature_columns]

    # Scale the customer data
    customer_scaled = scaler.transform(customer_data)

    # Make prediction
    prediction = model.predict(customer_scaled)

    # Get churn probability
    probability = model.predict_proba(customer_scaled)[0][1]

    # Get prediction value
    result = prediction[0]

    # Display result
    print("Churn Prediction:", result)
    print("Churn Probability:", probability)

    return result, probability