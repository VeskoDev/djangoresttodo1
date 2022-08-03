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


class Tag(models.Model):
    
    name = models.CharField(max_length=255)
    #image = models.ImageField(upload_to="Images/", default="Images/None/no-img.jpg")
    
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    tag = models.ManyToManyField('Tag')
    participants = models.ManyToManyField('Participant')

    def __str__(self):
        return self.title



    

class Participant(models.Model):
    
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    description = models.TextField(blank=True)
    titles = models.ForeignKey('Title', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Title(models.Model):
    
    name = models.CharField(max_length=255)
    participants = models.ForeignKey('Participant', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    


# """New part of code"""

# class Paradigm(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name
    

# class Language(models.Model):
#     name = models.CharField(max_length=255)
#     paradigm = models.ForeignKey('Paradigm', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name



# class Programmer(models.Model):
#     name = models.CharField(max_length=255)
#     language = models.ManyToManyField('Language')

#     def __str__(self):
#         return self.name