
from django import forms
from duttaEcommerceapp.models.jobseekermodel import JobSeekerUser

CHALLENGE_CHOICES = [
    ('Intense Competition', 'Intense Competition'),
    ('Skill Gaps', 'Skill Gaps'),
    ('Networking Challenges', 'Networking Challenges'),
    ('Automated Systems', 'Automated Systems'),
    ('Interview Stress', 'Interview Stress'),
    ('Economic Conditions', 'Economic Conditions'),
    ('Geographical Limitations', 'Geographical Limitations'),
    ('Personal Circumstances', 'Personal Circumstances'),
    ('Maintaining Motivation', 'Maintaining Motivation'),
]

class JobSeekerUserForm(forms.ModelForm):
    challenges = forms.MultipleChoiceField(
        choices=CHALLENGE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta:
        model = JobSeekerUser
        fields = ['story', 'challenges', 'achievements']
        widgets = {
            'story': forms.Textarea(attrs={
                'placeholder': 'Tell your story...', 
                'maxlength': 150, 
                'style': 'resize:none; width:50%; height:50px;'
            }),
            'achievements': forms.Textarea(attrs={
                'placeholder': 'Tell your achievements...', 
                'maxlength': 150, 
                'style': 'resize:none; width:50%; height:50px;'
            }),
        }
