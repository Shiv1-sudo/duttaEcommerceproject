# jobseekerforms.py
from django import forms
from duttaEcommerceapp.models.jobseekermodel import JobSeekerUser

class JobSeekerUserForm(forms.ModelForm):
    class Meta:
        model = JobSeekerUser
        fields = ['story', 'challenges', 'achievements']
        widgets = {
            'story': forms.Textarea(attrs={'placeholder': 'Tell your story...', 'maxlength': 500}),
            'challenges': forms.Textarea(attrs={'placeholder': 'Tell your challenges...', 'maxlength': 500}),
            'achievements': forms.Textarea(attrs={'placeholder': 'Tell your achievements...', 'maxlength': 500}),
        }
