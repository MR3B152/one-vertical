from django.db import models
from django.utils.translation import gettext as _


class TransactionStatus(models.IntegerChoices):
    Pending = 0, _('Pending')
    Completed = 1, _('Completed')


class PaymentMethod(models.IntegerChoices):
    stripe = 1, _('Stripe')
    Paypal = 2, _('Paypal')


class Transaction(models.Model):
    session = models.CharField(max_length=255)
    amount = models.FloatField()
    items = models.JSONField()
    customer = models.JSONField()
    status = models.IntegerField(
        choices=TransactionStatus.choices, default=TransactionStatus.Pending
    )
    payment_method = models.IntegerField(
        choices=TransactionStatus.choices
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def customer_name(self):
        return self.customer['first_name'] + ' ' + self.customer['last_name']
    
    @property
    def customer_email(self):
        return self.customer['email']