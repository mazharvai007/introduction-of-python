# Abstraction - Abstraction means hiding the complex implementation details and showing only the necessary features of an object

from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def format_message(self, message):
        """Format the message for the specific notification type."""
        pass

    @abstractmethod
    def send(self, message):
        """Send the formatted message...."""
        pass


class EmailNotification(Notification):
    def format_message(self, message):
        return f"Subject: Notification: {message}"

    def send(self, message):
        formatted_message = self.format_message(message)
        print(f"Sending Email: {formatted_message}")


class SMSNotification(Notification):
    def format_message(self, message):
        return f"SMS: {message}"

    def send(self, message):
        formatted_message = self.format_message(message)
        print(f"Sending SMS: {formatted_message}")


class PushNotification(Notification):
    def format_message(self, message):
        return f"Push Notification: {message}"

    def send(self, message):
        formatted_message = self.format_message(message)
        print(f"Sending Push Notification: {formatted_message}")


# Usages Example
def notify_user(notification: Notification, message):
    notification.send(message)


# Create instances of different notification types
email_notification = EmailNotification()
sms_notification = SMSNotification()
push_notification = PushNotification()

# Send notifications using the common interface
notify_user(email_notification, "You have a new email!")
notify_user(sms_notification, "You have a new SMS!")
notify_user(push_notification, "You have a new push notification")
