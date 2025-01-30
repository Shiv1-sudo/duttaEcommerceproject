# jobseekerforms.py
from django import forms
from duttaEcommerceapp.models.jobseekermodel import JobSeekerUser


class UserForm(forms.ModelForm):
    class Meta:
        model = JobSeekerUser
        fields = ['name', 'email', 'story', 'challenges', 'achievements']
