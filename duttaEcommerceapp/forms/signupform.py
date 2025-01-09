# duttaEcommerceapp/forms/signupform.py
# duttaEcommerceapp/forms/signupform.py
'''from django import forms
from django.contrib.auth.forms import UserCreationForm
from duttaEcommerceapp.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        })
    )
    middle_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Middle Name'
        })
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address'
        })
    )
    phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone Number'
        }),
        help_text='Enter a valid phone number'
    )
    address = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Address',
            'rows': 4
        })
    )
    
    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'address', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password'
            })
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.middle_name = self.cleaned_data['middle_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.address = self.cleaned_data['address']
        if commit:
            user.save()
        return user'''
from django import forms
from django.contrib.auth.forms import UserCreationForm
from duttaEcommerceapp.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'First Name',
            'style': 'background-color: #ffffff; color: #333; border: 1px solid #ccc;'
        })
    )
    middle_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Middle Name',
            'style': 'background-color: #ffffff; color: #333; border: 1px solid #ccc;'
        })
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Last Name',
            'style': 'background-color: #ffffff; color: #333; border: 1px solid #ccc;'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Email Address',
            'style': 'background-color: #ffffff; color: #333; border: 1px solid #ccc;'
        })
    )
    phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Phone Number',
            'style': 'background-color: #ffffff; color: #333; border: 1px solid #ccc;'
        }),
        help_text='Enter a valid phone number'
    )
    address = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Address',
            'rows': 4,
            'style': 'background-color: #ffffff; color: #333; border: 1px solid #ccc;'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'address', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Password',
                'style': 'background-color: #ffffff; color: #333; border: 1px solid #ccc;'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Confirm Password',
                'style': 'background-color: #ffffff; color: #333; border: 1px solid #ccc;'
            })
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.middle_name = self.cleaned_data['middle_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.address = self.cleaned_data['address']
        if commit:
            user.save()
            print(f"User {user.email} saved successfully!")
        return user
