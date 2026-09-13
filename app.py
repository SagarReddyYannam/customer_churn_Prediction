import streamlit as st
import pandas as pd

from src.predict import predict_churn

st.title("Customer Churn Prediction")

st.write("Enter customer details below:")

tenure = st.number_input("Tenure", min_value=0, value=12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=840.0)

senior_citizen = st.selectbox("Senior Citizen", [0, 1])
gender_male = st.selectbox("Gender Male", [0, 1])
partner_yes = st.selectbox("Partner", [0, 1])
dependents_yes = st.selectbox("Dependents", [0, 1])
phone_service_yes = st.selectbox("Phone Service", [0, 1])

multiple_lines_no_phone = st.selectbox("Multiple Lines - No phone service", [0, 1])
multiple_lines_yes = st.selectbox("Multiple Lines - Yes", [0, 1])

internet_fiber = st.selectbox("Internet Service - Fiber optic", [0, 1])
internet_no = st.selectbox("Internet Service - No", [0, 1])

online_security_no = st.selectbox("Online Security - No internet service", [0, 1])
online_security_yes = st.selectbox("Online Security - Yes", [0, 1])

online_backup_no = st.selectbox("Online Backup - No internet service", [0, 1])
online_backup_yes = st.selectbox("Online Backup - Yes", [0, 1])

device_protection_no = st.selectbox("Device Protection - No internet service", [0, 1])
device_protection_yes = st.selectbox("Device Protection - Yes", [0, 1])

tech_support_no = st.selectbox("Tech Support - No internet service", [0, 1])
tech_support_yes = st.selectbox("Tech Support - Yes", [0, 1])

streaming_tv_no = st.selectbox("Streaming TV - No internet service", [0, 1])
streaming_tv_yes = st.selectbox("Streaming TV - Yes", [0, 1])

streaming_movies_no = st.selectbox("Streaming Movies - No internet service", [0, 1])
streaming_movies_yes = st.selectbox("Streaming Movies - Yes", [0, 1])

contract_one_year = st.selectbox("Contract - One year", [0, 1])
contract_two_year = st.selectbox("Contract - Two year", [0, 1])

paperless_billing_yes = st.selectbox("Paperless Billing", [0, 1])

payment_credit_card = st.selectbox(
    "Payment Method - Credit card (automatic)", [0, 1]
)

payment_electronic = st.selectbox(
    "Payment Method - Electronic check", [0, 1]
)

payment_mailed = st.selectbox(
    "Payment Method - Mailed check", [0, 1]
)

if st.button("Predict Churn"):

    customer_data = pd.DataFrame([{
        "SeniorCitizen": senior_citizen,
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "gender_Male": gender_male,
        "Partner_Yes": partner_yes,
        "Dependents_Yes": dependents_yes,
        "PhoneService_Yes": phone_service_yes,
        "MultipleLines_No phone service": multiple_lines_no_phone,
        "MultipleLines_Yes": multiple_lines_yes,
        "InternetService_Fiber optic": internet_fiber,
        "InternetService_No": internet_no,
        "OnlineSecurity_No internet service": online_security_no,
        "OnlineSecurity_Yes": online_security_yes,
        "OnlineBackup_No internet service": online_backup_no,
        "OnlineBackup_Yes": online_backup_yes,
        "DeviceProtection_No internet service": device_protection_no,
        "DeviceProtection_Yes": device_protection_yes,
        "TechSupport_No internet service": tech_support_no,
        "TechSupport_Yes": tech_support_yes,
        "StreamingTV_No internet service": streaming_tv_no,
        "StreamingTV_Yes": streaming_tv_yes,
        "StreamingMovies_No internet service": streaming_movies_no,
        "StreamingMovies_Yes": streaming_movies_yes,
        "Contract_One year": contract_one_year,
        "Contract_Two year": contract_two_year,
        "PaperlessBilling_Yes": paperless_billing_yes,
        "PaymentMethod_Credit card (automatic)": payment_credit_card,
        "PaymentMethod_Electronic check": payment_electronic,
        "PaymentMethod_Mailed check": payment_mailed
    }])

    result, probability = predict_churn(customer_data)

    if result == "Yes":
        st.error(f"⚠️ Customer likely to churn")
    else:
        st.success(f"✅ Customer likely to stay")

    st.write(f"Churn probability: **{probability:.2%}**")