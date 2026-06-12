# CreditWise AI – Loan Approval System
CreditWise AI is a Machine Learning-based loan approval system designed to predict whether a loan application should be approved or rejected based on applicant details.

## Project Overview

CreditWise AI is a Machine Learning-based system that predicts whether a loan application should be approved or rejected based on applicant details such as income, credit history, and other financial attributes.

This project aims to automate the loan approval process, making it faster, more consistent, and data-driven.

## Problem Statement

Traditional loan approval processes are:

- Time-consuming 
- Prone to human bias 
- Inconsistent in decision-making

This system solves these issues by using Machine Learning models to provide accurate and reliable predictions.

## Dataset Structure
### Categorical Columns:

Employment_Status, Marital_Status, Loan_Purpose, Property_Area, Education_Level, Gender, Employer_Category, Loan_Approved.

### Numerical Columns:

Applicant_ID, Applicant_Income, Coapplicant_Income, Age, Dependents, Credit_Score, Existing_Loans, DTI_Ratio, Savings, Collateral_Value, Loan_Amount, Loan_Term


## Tech Stack
### Language: 
Python

### Libraries:
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Label Encoder

### Model Used: 
- Logistic Regression
- Random Forest
- Naive Bayes Classifier



## Project Workflow

- Data Collection
- Data Preprocessing
- Handling missing values
- Encoding categorical variables
- Exploratory Data Analysis (EDA)
- Visualizing categorical variables
- Outlier Detection in numerical variables
- Correlation Heatmap
- Feature Scaling & Engineering
- Model Building
- Model Training and Evaluation
- Feature Engineering to improve the model evaluation metrics.


## Results

- Logistic Regression : 74.5%
- Random Forest       : 91.5%
- Naive Bayes         : 73.0%

Best Model selected from the above 3 models - Random Forest


Model Accuracy: 91.5%

- Reduced manual effort in loan approval
- Faster and consistent decision-making
  
## Project Structure
SmartLoan AI_Loan_Approval_System

- ├── data/                  # Dataset files
- ├── notebooks/            # Jupyter notebooks
- └── README.md             # Project documentation
- └── accuracies            # accuracies of model
- └── app.py                # Streamlit UI code
- └── EDA.ipynb             # Exploratory data analysis
- └── encoders.json         # Encoders for categorical columns
- └── requirements.txt      
- └── train_model.py        # training model 


## Future Enhancement:
- Add interactive dashboard
- Use advanced ML models (XGBoost, Neural Networks)
- Improve fairness and bias detection


## Author

Sejal Naik

- Aspiring Data Analyst and Data Scientist
- Skilled in SQL, Python, Power BI, Machine Learning.
- 🔗 LinkedIn: https://www.linkedin.com/in/sejalnaik-/
- 📧 Email: sejal.naik312003@gmail.com
