import logging

def respond_to_intrusion(activity):
    """
    Handles responses to suspicious activities.
    """
    logging.error(f"Suspicious activity detected: {activity}")
    # Actions like alerting the admin or blocking the user
    print("Alert! Taking necessary action.")