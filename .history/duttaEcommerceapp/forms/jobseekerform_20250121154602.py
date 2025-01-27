'''from django import forms
from duttaEcommerceapp.models.jobseekermodel import JobSeekerUser

class JobSeekerUserForm(forms.ModelForm):
    class Meta:
        model = JobSeekerUser
        fields = ['story', 'challenges', 'achievements']
        widgets = {
            'story': forms.Textarea(attrs={
                'placeholder': 'Tell your story...', 
                'maxlength': 250, 
                'style': 'resize:none; width:100%; height:100px;'
            }),
            'challenges': forms.Textarea(attrs={
                'placeholder': 'Tell your challenges...', 
                'maxlength': 250, 
                'style': 'resize:none; width:100%; height:100px;'
            }),
            'achievements': forms.Textarea(attrs={
                'placeholder': 'Tell your achievements...', 
                'maxlength': 250, 
                'style': 'resize:none; width:100%; height:100px;'
            }),
        }
'''