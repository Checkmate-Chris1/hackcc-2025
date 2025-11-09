import numpy as np
import pandas as pd
from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import CountVectorizer

df=pd.read_csv(r"disease_dataset.csv")
print(df.shape)
print(df.columns)


X = df.drop(columns=["diseases"])
y = df["diseases"]

# Remove classes with less than 2 samples
counts = y.value_counts()
valid_classes = counts[counts >= 2].index
X = X[y.isin(valid_classes)]
y = y[y.isin(valid_classes)]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=0, stratify=y
)

from sklearn.naive_bayes import BernoulliNB
bnb = BernoulliNB()
model = bnb.fit(X_train, y_train)
y_pred = bnb.predict(X_test)

from sklearn.metrics import classification_report, accuracy_score
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

import joblib
joblib.dump(model, "doctor.pkl")
joblib.dump(X.columns.tolist(), "doctor_columns.pkl")
