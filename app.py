import streamlit as st
import pandas as pd
import joblib
import json

# Load model
model = joblib.load("loan_model.pkl")

# Load encoders
with open("encoders.json", "r") as f:
    encoders = json.load(f)

st.set_page_config(page_title="Loan Approval Prediction")

st.title("🏦 Loan Approval Prediction System")

# Inputs
applicant_income = st.number_input("Applicant Income", min_value=0)

coapplicant_income = st.number_input("Coapplicant Income", min_value=0)

employment_status = st.selectbox(
    "Employment Status",
    encoders["Employment_Status"]["classes"]
)

age = st.number_input("Age", min_value=18, max_value=100)

marital_status = st.selectbox(
    "Marital Status",
    encoders["Marital_Status"]["classes"]
)

dependents = st.number_input("Dependents", min_value=0, max_value=10)

credit_score = st.number_input(
    "Credit Score",
    min_value=300,
    max_value=900
)

existing_loans = st.number_input(
    "Existing Loans",
    min_value=0,
    max_value=20
)

dti_ratio = st.number_input(
    "DTI Ratio",
    min_value=0.0,
    max_value=1.0
)

savings = st.number_input("Savings", min_value=0)

collateral_value = st.number_input(
    "Collateral Value",
    min_value=0
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0
)

loan_term = st.number_input(
    "Loan Term",
    min_value=1
)

loan_purpose = st.selectbox(
    "Loan Purpose",
    encoders["Loan_Purpose"]["classes"]
)

property_area = st.selectbox(
    "Property Area",
    encoders["Property_Area"]["classes"]
)

education_level = st.selectbox(
    "Education Level",
    encoders["Education_Level"]["classes"]
)

gender = st.selectbox(
    "Gender",
    encoders["Gender"]["classes"]
)

employer_category = st.selectbox(
    "Employer Category",
    encoders["Employer_Category"]["classes"]
)

if st.button("Predict Loan Status"):

    # Encode categorical inputs
    employment_status_encoded = encoders["Employment_Status"]["classes"].index(employment_status)

    marital_status_encoded = encoders["Marital_Status"]["classes"].index(marital_status)

    loan_purpose_encoded = encoders["Loan_Purpose"]["classes"].index(loan_purpose)

    property_area_encoded = encoders["Property_Area"]["classes"].index(property_area)

    education_level_encoded = encoders["Education_Level"]["classes"].index(education_level)

    gender_encoded = encoders["Gender"]["classes"].index(gender)

    employer_category_encoded = encoders["Employer_Category"]["classes"].index(employer_category)

    # Create dataframe
    input_data = pd.DataFrame([[
        applicant_income,
        coapplicant_income,
        employment_status_encoded,
        age,
        marital_status_encoded,
        dependents,
        credit_score,
        existing_loans,
        dti_ratio,
        savings,
        collateral_value,
        loan_amount,
        loan_term,
        loan_purpose_encoded,
        property_area_encoded,
        education_level_encoded,
        gender_encoded,
        employer_category_encoded
    ]], columns=[
        "Applicant_Income",
        "Coapplicant_Income",
        "Employment_Status",
        "Age",
        "Marital_Status",
        "Dependents",
        "Credit_Score",
        "Existing_Loans",
        "DTI_Ratio",
        "Savings",
        "Collateral_Value",
        "Loan_Amount",
        "Loan_Term",
        "Loan_Purpose",
        "Property_Area",
        "Education_Level",
        "Gender",
        "Employer_Category"
    ])

    # Prediction
    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")

    # Reasons
    st.subheader("Reason Behind Prediction")

    if credit_score >= 750:
        st.write("✔ Good Credit Score")
    else:
        st.write("❌ Low Credit Score")

    if applicant_income + coapplicant_income >= 70000:
        st.write("✔ Strong Income")
    else:
        st.write("❌ Low Income")

    if dti_ratio <= 0.35:
        st.write("✔ Healthy DTI Ratio")
    else:
        st.write("❌ High DTI Ratio")

    if savings >= 100000:
        st.write("✔ Good Savings")
    else:
        st.write("❌ Low Savings")

    if existing_loans <= 1:
        st.write("✔ Low Existing Loans")
    else:
        st.write("❌ Too Many Existing Loans")
