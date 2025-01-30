# jobseekermodels.py
from django.db import models

class JobSeekerUser(models.Model):
    '''name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)'''
    story = models.TextField()
    challenges = models.TextField()
    achievements = models.TextField()

    def __str__(self):
        return self.name
