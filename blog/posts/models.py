from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField(max_length=600)

    def __str__(self) -> str:
        return f"{self.title}"
