import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import os
import joblib
import re

# ----------------------
# Load dataset
# ----------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "disease_dataset.csv")
df = pd.read_csv(csv_path)

# ----------------------
# Clean column names
# ----------------------
df.columns = [re.sub(r'[^A-Za-z0-9_]', '_', col) for col in df.columns]

# ----------------------
# Prepare features/labels
# ----------------------
X = df.drop(columns=["diseases"])
y = df["diseases"]

counts = y.value_counts()
valid_classes = counts[counts >= 2].index
X = X[y.isin(valid_classes)]
y = y[y.isin(valid_classes)]

# Remove all-zero columns
X = X.loc[:, (X.sum(axis=0) > 0)]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ----------------------
# Train Logistic Regression
# ----------------------
model = LogisticRegression(
    solver="liblinear",
    max_iter=1000,
    multi_class="auto",
    verbose=1
)
model.fit(X_train, y_train)

# ----------------------
# Evaluate
# ----------------------
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy on test set: {accuracy:.4f}")
print(classification_report(y_test, y_pred))

# ----------------------
# Save model
# ----------------------
joblib.dump(model, os.path.join(BASE_DIR, "doctor.pkl"))
print("The doctor is in!")

# ----------------------
# Optional: predict function
# ----------------------
def predict_disease(user_symptoms):
    """
    user_symptoms: list or array of 0s and 1s (same order as X.columns)
    """
    import numpy as np
    X_input = np.array(user_symptoms).reshape(1, -1)
    prediction = model.predict(X_input)[0]
    confidence = model.predict_proba(X_input).max()
    return {
        "predicted_disease": prediction,
        "confidence": float(confidence)
    }
