from django.db import models

class TechService(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.CharField(max_length=100)
    link = models.URLField()
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name
