from django import forms
from duttaEcommerceapp.models.paymentmodel import Payment
from duttaEcommerceapp.models.paymentmodel import Payment
from django_countries.widgets import CountrySelectWidget


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'mode_of_payment', 'card_number', 'card_expiry', 'card_cvv',
            'address', 'postal_code', 'country', 'contact_number',
            'name', 'email', 'landmark'
        ]
        widgets = {
            'mode_of_payment': forms.Select(attrs={'id': 'payment_mode', 'onchange': 'showPaymentFields(this.value)'}),
            'card_number': forms.PasswordInput(attrs={'maxlength': 16, 'id': 'id_card_number', 'autocomplete': 'off', 'pattern': '[0-9]*', 'inputmode': 'numeric'}),
            'card_expiry': forms.TextInput(attrs={'maxlength': 5, 'id': 'id_card_expiry', 'placeholder': 'MM/YY', 'pattern': '(0[1-9]|1[0-2])\/?([0-9]{2})'}),
            'card_cvv': forms.PasswordInput(attrs={'maxlength': 3, 'id': 'id_card_cvv', 'autocomplete': 'off', 'pattern': '[0-9]*', 'inputmode': 'numeric'}),
            'address': forms.Textarea(attrs={'id': 'id_address', 'rows': 3, 'cols': 40, 'style': 'resize:none;'}),
            'postal_code': forms.TextInput(attrs={'maxlength': 10, 'id': 'id_postal_code', 'oninput': 'validatePostalCode(this)'}),
            'country': CountrySelectWidget(attrs={'id': 'id_country'}),
            'contact_number': forms.TextInput(attrs={'maxlength': 15, 'id': 'id_contact_number', 'pattern': '[0-9]*', 'inputmode': 'numeric'}),
            'name': forms.TextInput(attrs={'maxlength': 100, 'id': 'id_name'}),
            'email': forms.EmailInput(attrs={'id': 'id_email'}),
            'landmark': forms.TextInput(attrs={'maxlength': 100, 'id': 'id_landmark'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mode_of_payment'].widget.attrs.update({
            'onchange': 'showPaymentFields(this.value)'
        })

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})