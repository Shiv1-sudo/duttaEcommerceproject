# jobseekerforms.py
from django import forms
'''from duttaE.models.jobseekermodel import User'''

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'story', 'challenges', 'achievements']
