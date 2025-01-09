from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from duttaEcommerceapp.models.models import User
'''from django import forms'''
'''from duttaEcommerceapp.models.paymentmodel import Payment

from django_countries.widgets import CountrySelectWidget'''  # Assuming you're using django-countries


'''class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
'''
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
'''class ForgotPasswordForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
'''



'''class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['mode_of_payment', 'card_number', 'card_expiry', 'card_cvv', 'address', 'postal_code', 'country', 'contact_number', 'name', 'email', 'landmark']
        widgets = {
            'mode_of_payment': forms.Select(attrs={'id': 'payment_mode', 'onchange': 'showPaymentFields(this.value)'}),
            'card_number': forms.TextInput(attrs={'maxlength': 16, 'id': 'id_card_number'}),
            'card_expiry': forms.TextInput(attrs={'maxlength': 5, 'id': 'id_card_expiry'}),
            'card_cvv': forms.TextInput(attrs={'maxlength': 3, 'id': 'id_card_cvv'}),
            'address': forms.Textarea(attrs={'id': 'id_address'}),
            'postal_code': forms.TextInput(attrs={'maxlength': 10, 'id': 'id_postal_code'}),
            'country': forms.TextInput(attrs={'maxlength': 50, 'id': 'id_country'}),
            'contact_number': forms.TextInput(attrs={'maxlength': 15, 'id': 'id_contact_number'}),
            'name': forms.TextInput(attrs={'maxlength': 100, 'id': 'id_name'}),
            'email': forms.EmailInput(attrs={'id': 'id_email'}),
            'landmark': forms.TextInput(attrs={'maxlength': 100, 'id': 'id_landmark'}),
        }
'''


'''class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['mode_of_payment', 'card_number', 'card_expiry', 'card_cvv', 'address', 'postal_code', 'country', 'contact_number', 'name', 'email', 'landmark']
        widgets = {
            'mode_of_payment': forms.Select(attrs={'id': 'payment_mode', 'onchange': 'showPaymentFields(this.value)'}),
            'card_number': forms.PasswordInput(attrs={'maxlength': 16, 'id': 'id_card_number', 'autocomplete': 'off', 'pattern': '[0-9]*', 'inputmode': 'numeric'}),
            'card_expiry': forms.TextInput(attrs={'maxlength': 5, 'id': 'id_card_expiry', 'placeholder': 'MM/YY', 'pattern': '(0[1-9]|1[0-2])\/?([0-9]{2})'}),
            'card_cvv': forms.PasswordInput(attrs={'maxlength': 3, 'id': 'id_card_cvv', 'autocomplete': 'off', 'pattern': '[0-9]*', 'inputmode': 'numeric'}),
            'address': forms.Textarea(attrs={'id': 'id_address', 'rows': 3, 'cols': 40}),
            'postal_code': forms.TextInput(attrs={'maxlength': 10, 'id': 'id_postal_code', 'oninput': 'validatePostalCode(this)'}),
            'country': CountrySelectWidget(attrs={'id': 'id_country'}),
            'contact_number': forms.TextInput(attrs={'maxlength': 15, 'id': 'id_contact_number', 'list': 'phone_extensions'}),
            'name': forms.TextInput(attrs={'maxlength': 100, 'id': 'id_name'}),
            'email': forms.EmailInput(attrs={'id': 'id_email'}),
            'landmark': forms.TextInput(attrs={'maxlength': 100, 'id': 'id_landmark'}),
        }'''
