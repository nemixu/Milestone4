from django.http import HttpResponse


class StripeWH_Handler: 
    """Handle stripe webhooks"""
    
    def __init__(self, request):
        self.request = request
            
    def handle_event(self, event):
        """Handle webhook event """
        
        return HttpResponse(
            content=f'Unhandled webhook recevied: {event["type"]}',
            status=200)
        
    def handle_payment_intent_succeeded(self, event):
        """Handle payment_intent.suceeded webhook from stripe"""
        
        return HttpResponse(
            content=f'Webhook recevied: {event["type"]}',
            status=200)    
        
    def handle_payment_intent_payment_failed(self, event):
        """Handle payment_intent.failed webhook from stripe"""
        
        return HttpResponse(
            content=f'Webhook recevied: {event["type"]}',
            status=200)        