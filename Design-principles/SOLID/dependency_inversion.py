class EmailService:
    def send_message(self, message: str):
        print(f"Sending email: {message}")

class SMSService:
    def send_message(self, message: str):
        print(f"Sending SMS: {message}")
    
    def compress_message(self, message: str):
        return "compressed: " + message 

class NotificationManager:
    def __init__(self, notification_type: str):
        if notification_type == "email":
            self.service = EmailService()
        elif notification_type == "sms":
            self.service = SMSService()
        else:
            raise ValueError("Invalid notification type")

    def log(self):
        pass

    def send_notification(self, message: str):
        self.log()
        if isinstance(self.service, SMSService):
            message = self.service.compress_message(message)
        self.service.send_message(message)

# Usage
if __name__ == "__main__":
    # Using Email Service
    email_manager = NotificationManager("email")
    email_manager.send_notification("Hello via email!")

    # Using SMS Service
    sms_manager = NotificationManager("sms")
    sms_manager.send_notification("Hello via SMS!")