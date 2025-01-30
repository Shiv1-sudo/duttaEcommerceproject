# jobseekermodels.py
from django.db import models

class JobSeekerUser(models.Model):
    '''name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)'''
    story = models.TextField()
    challenges = models.TextField() #store challenges as comma
    achievements = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.story[:50]
#Table for saving comment data at jabseeker page
class JobSeekerComment(models.Model):
    job_seeker_user = models.ForeignKey(JobSeekerUser, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text[:50]
