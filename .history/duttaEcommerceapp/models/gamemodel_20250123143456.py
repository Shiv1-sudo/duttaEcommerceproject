'''from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=255)
    explanation = models.TextField()

    def __str__(self):
        return self.question_text

class UserScore(models.Model):
    game_user = models.ForeignKey(User, on_delete=models.CASCADE)  # Renamed field
    score = models.IntegerField(default=0)
    last_played = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.game_user.username} - {self.score}"
'''
from django.db import models
from django.conf import settings  # Import settings to access AUTH_USER_MODEL

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(maxlength=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=255)
    explanation = models.TextField()

    def __str__(self):
        return self.question_text

class UserScore(models.Model):
    game_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use AUTH_USER_MODEL
    score = models.IntegerField(default=0)
    last_played = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.game_user.username} - {self.score}"

