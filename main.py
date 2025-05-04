import logging
from data_preprocessing import preprocess_data
from anomaly_detection import train_model, detect_intrusion
from response_handler import respond_to_intrusion

def main():
    logging.info("Starting Cybersecurity AI program...")
    
    # Example user activity data
    user_activity_data = ["login", "download_file", "visit_sensitive_page", "upload_file"]
    
    # Preprocessing data
    processed_data = preprocess_data(user_activity_data)
    
    # Training model
    model = train_model(processed_data)
    
    while True:
        new_activity = input("Enter a new activity (e.g., 'delete_file'): ")
        is_suspicious = detect_intrusion(model, new_activity)
        
        if is_suspicious:
            respond_to_intrusion(new_activity)
        else:
            logging.info("Activity is normal.")
        
if _name_ == "_main_":
    main()