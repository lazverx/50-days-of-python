# Day 12 – Abstract Base Classes

**Date:** 2025-09-09  

## What I Learned
- How to define **abstract base classes (ABC)** in Python using `abc.ABC` and `@abstractmethod`.
- Enforcing a **contract** for subclasses, ensuring consistent implementation.
- How attempting to instantiate an incomplete subclass raises a `TypeError`.

## Tasks Completed
- Implemented `PaymentProcessor` as an abstract base class.
- Created two valid implementations:
  - `CreditCardProcessor`
  - `PayPalProcessor`
- Demonstrated an incomplete class (`IncompleteProcessor`) that fails because it doesn’t implement all abstract methods.

## Files
- `payments.py` → Contains the abstract base class and implementations.

## How to Run
```bash
python payments.py
