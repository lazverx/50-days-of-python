from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    """Abstract Base Class for different payment processors."""

    @abstractmethod
    def authenticate(self, api_key: str) -> bool:
        """Authenticate the processor with API key."""
        pass

    @abstractmethod
    def pay(self, amount: float) -> None:
        """Process a payment of given amount."""
        pass


class CreditCardProcessor(PaymentProcessor):
    def authenticate(self, api_key: str) -> bool:
        print(f"[CreditCard] Authenticating with API key: {api_key}")
        return True

    def pay(self, amount: float) -> None:
        print(f"[CreditCard] Paid ${amount:.2f} using credit card.")


class PayPalProcessor(PaymentProcessor):
    def authenticate(self, api_key: str) -> bool:
        print(f"[PayPal] Authenticating with API key: {api_key}")
        return True

    def pay(self, amount: float) -> None:
        print(f"[PayPal] Paid ${amount:.2f} using PayPal.")


# ❌ This class will raise an error if instantiated,
#    because it doesn't implement 'pay'
class IncompleteProcessor(PaymentProcessor):
    def authenticate(self, api_key: str) -> bool:
        return True


if __name__ == "__main__":
    cc = CreditCardProcessor()
    cc.authenticate("cc_api_key_123")
    cc.pay(50)

    paypal = PayPalProcessor()
    paypal.authenticate("paypal_api_key_456")
    paypal.pay(75)

    # Uncommenting below will raise error:
    # incomplete = IncompleteProcessor()
