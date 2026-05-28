import pandas as pd
import joblib
import json

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("loan_approval_data.csv")

# Remove ID column
df.drop("Applicant_ID", axis=1, inplace=True)

# Fill missing values
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())

# Encode categorical columns
label_encoders = {}

for col in df.columns:
    if df[col].dtype == "object":
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))

        label_encoders[col] = list(le.classes_)

# Features and target
X = df.drop("Loan_Approved", axis=1)
y = df["Loan_Approved"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Models
lr_model = LogisticRegression(max_iter=5000)
rf_model = RandomForestClassifier(n_estimators=200, random_state=42)
nb_model = GaussianNB()

# Train models
lr_model.fit(X_train, y_train)
rf_model.fit(X_train, y_train)
nb_model.fit(X_train, y_train)

# Predictions
lr_pred = lr_model.predict(X_test)
rf_pred = rf_model.predict(X_test)
nb_pred = nb_model.predict(X_test)

# Accuracy
lr_acc = round(accuracy_score(y_test, lr_pred) * 100, 2)
rf_acc = round(accuracy_score(y_test, rf_pred) * 100, 2)
nb_acc = round(accuracy_score(y_test, nb_pred) * 100, 2)

print("Logistic Regression Accuracy:", lr_acc)
print("Random Forest Accuracy:", rf_acc)
print("Naive Bayes Accuracy:", nb_acc)

# Save best model
joblib.dump(rf_model, "loan_model.pkl")

# Save encoders
with open("encoders.json", "w") as f:
    json.dump(label_encoders, f)
