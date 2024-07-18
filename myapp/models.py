from django.db import models

class Review(models.Model):
    username = models.CharField(max_length=30)
    text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.username