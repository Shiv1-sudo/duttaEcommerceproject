
from django.db import models
from django_countries.fields import CountryField  # Import CountryField from django_countries

class Payment(models.Model):
    MODE_OF_PAYMENT_CHOICES = [
        ('debit_card', 'Debit Card'),
        ('credit_card', 'Credit Card'),
        ('cash_on_delivery', 'Cash on Delivery'),
    ]

    mode_of_payment = models.CharField(max_length=20, choices=MODE_OF_PAYMENT_CHOICES)
    card_number = models.CharField(max_length=16, null=True, blank=True)
    card_expiry = models.CharField(max_length=5, null=True, blank=True)  # Format: MM/YY
    card_cvv = models.CharField(max_length=3, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    country = CountryField(blank_label='(select country)')  # Use CountryField here
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    landmark = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Payment {self.id} - {self.mode_of_payment}"
