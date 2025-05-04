from sklearn.ensemble import IsolationForest
import logging

def train_model(activity_vector):
    """
    Trains the anomaly detection model.
    """
    model = IsolationForest(contamination=0.1)
    model.fit(activity_vector)
    logging.info("Model trained successfully.")
    return model

def detect_intrusion(model, new_activity_vector):
    """
    Detects intrusion based on new activity.
    """
    prediction = model.predict(new_activity_vector)
    return prediction == -1