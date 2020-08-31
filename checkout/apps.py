from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Checkout name and handle the ready function
    """
    name = 'checkout'

    def ready(self):
        import checkout.signals