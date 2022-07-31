from django.db import models
from helpers.models import TrackingModel
from authentication.models import User 


class Todo(TrackingModel):
    title = models.CharField(max_length=255)
    description = models.TextField(default="Vesko")
    is_complete = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title



class Tag(models.Model):

    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name