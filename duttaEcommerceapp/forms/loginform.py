
from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

class OTPForm(forms.Form):
    otp = forms.CharField(label='OTP', max_length=6)
