import joblib
import numpy as np

# Load trained model and feature columns
model_doctor = joblib.load("doctor.pkl")
model_columns = joblib.load("doctor_columns.pkl")

# Example input: list of symptoms
user_symptoms = ["loss of sex drive", "premature ejaculation", "penis pain"]
def predict_top_diseases(user_symptoms_list, top_n=5):
    # Filter only symptoms that exist in the model
    valid_symptoms = set(model_columns)
    user_symptoms_filtered = [s for s in user_symptoms_list if s in valid_symptoms]

    # Build input vector
    X_input = [1 if symptom in user_symptoms_filtered else 0 for symptom in model_columns]
    X_input = np.array(X_input).reshape(1, -1)

    # Predict probabilities
    pred_probs = model_doctor.predict_proba(X_input)
    if isinstance(pred_probs, list):  # BernoulliNB returns a list for multi-class
        pred_probs = np.hstack(pred_probs)

    # Get top N diseases
    top_indices = pred_probs[0].argsort()[::-1][:top_n]
    top_diseases = [(model_doctor.classes_[i], float(pred_probs[0][i])) for i in top_indices]

    return top_diseases

if __name__ == "__main__":
    # Example usage
    result = predict_top_diseases(user_symptoms, top_n=5)
    for disease, confidence in result:
        print(f"Disease: {disease}, Confidence: {confidence:.4f}")
