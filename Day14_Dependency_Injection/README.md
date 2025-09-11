# Day 14 – Dependency Injection

**Date:** 2025-09-11  

## What I Learned
- **Dependency Injection (DI)** decouples code by separating high-level logic from low-level implementations.
- By injecting dependencies, we can easily **swap services** (Email, SMS, Push) without modifying core business logic.
- Using `Protocol` (from `typing`) allows us to define **interface-like contracts** in Python.
- DI improves **testability**, **flexibility**, and **maintainability** of applications.

## Tasks Completed
- Defined a `MessageSender` protocol as the base interface.
- Implemented three different message senders:
  - `EmailSender` → simulates SMTP email sending.
  - `SMSSender` → simulates telecom SMS delivery with random delay.
  - `PushNotificationSender` → simulates push notification (Firebase).
- Created `NotificationService` that depends on an injected `MessageSender`.
- Built a higher-level `UserNotifier` that uses the notification service to:
  - Welcome new users.
  - Send OTP codes.

## Files
- `depedencyinject.py` → Complete implementation of Dependency Injection.

## How to Run
```bash
python dependencyinject.py
