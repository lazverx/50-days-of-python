from typing import Protocol
import random
import time


# Define interface for senders
class MessageSender(Protocol):
    def send(self, recipient: str, message: str) -> None:
        ...


# Implementations
class EmailSender:
    def send(self, recipient: str, message: str) -> None:
        print(f"[Email] Connecting to SMTP server...")
        time.sleep(0.5)
        print(f"[Email] Sending to {recipient}: {message}")


class SMSSender:
    def send(self, recipient: str, message: str) -> None:
        print(f"[SMS] Connecting to Telecom Provider...")
        time.sleep(0.3)
        # simulate random delay
        delay = random.uniform(0.1, 0.5)
        time.sleep(delay)
        print(f"[SMS] Delivered to {recipient}: {message}")


class PushNotificationSender:
    def send(self, recipient: str, message: str) -> None:
        print(f"[Push] Sending push notification via Firebase...")
        time.sleep(0.4)
        print(f"[Push] Push notification sent to {recipient}: {message}")


# Service that depends on injected sender
class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def notify(self, recipient: str, message: str) -> None:
        self.sender.send(recipient, message)


# Higher level system using DI
class UserNotifier:
    """High-level class that does not depend on any concrete implementation."""

    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def welcome_user(self, username: str, contact: str) -> None:
        self.notification_service.notify(contact, f"Welcome {username}!")

    def send_otp(self, contact: str) -> None:
        otp = random.randint(100000, 999999)
        self.notification_service.notify(contact, f"Your OTP code is {otp}")


if __name__ == "__main__":
    # Example: send via Email
    email_service = NotificationService(EmailSender())
    user_notifier_email = UserNotifier(email_service)
    user_notifier_email.welcome_user("Alice", "alice@example.com")
    user_notifier_email.send_otp("alice@example.com")

    print("\n" + "-"*40 + "\n")

    # Example: send via SMS
    sms_service = NotificationService(SMSSender())
    user_notifier_sms = UserNotifier(sms_service)
    user_notifier_sms.welcome_user("Bob", "+62123456789")
    user_notifier_sms.send_otp("+62123456789")

    print("\n" + "-"*40 + "\n")

    # Example: send via Push Notification
    push_service = NotificationService(PushNotificationSender())
    user_notifier_push = UserNotifier(push_service)
    user_notifier_push.welcome_user("Charlie", "charlie_device_token")
    user_notifier_push.send_otp("charlie_device_token")
