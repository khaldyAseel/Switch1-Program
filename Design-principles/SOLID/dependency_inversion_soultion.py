from abc import ABC, abstractmethod

# Abstract base class for notification services
class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass

# Concrete implementations of notification services
class EmailService(NotificationService):
    def send_notification(self, message: str):
        print(f"Sending email: {message}")

class SMSService(NotificationService):
    def send_notification(self, message: str):
        compressed_message = self._compress_message(message) # inversion of control
        print(f"Sending SMS: {compressed_message}")
    
    def _compress_message(self, message: str):
        return "compressed: " + message 

# High-level module
class NotificationManager:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def log(self):
        pass

    def send_notification(self, message: str):
        self.log()
        self.notification_service.send_notification(message)

# Usage
if __name__ == "__main__":
    # Using Email Service
    email_service = EmailService()
    email_manager = NotificationManager(email_service)
    email_manager.send_notification("Hello via email!")

    # Using SMS Service
    sms_service = SMSService()
    sms_manager = NotificationManager(sms_service)
    sms_manager.send_notification("Hello via SMS!")