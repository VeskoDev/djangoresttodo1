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



class Slike(models.Model):
    
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class PrikazSlika(models.Model):
    
    #album = models.ForeignKey('Slike', related_name='albums', null=True, blank=True, on_delete=models.CASCADE)
    ime = models.CharField(max_length=255)
    slika = models.ImageField(null=True, blank=True)

       


    def __str__(self):
        return self.ime + self.slika




class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    participants = models.ManyToManyField('Participant')

    def __str__(self):
        return self.title



    

class Participant(models.Model):
    
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)  
    description = models.TextField(blank=True)
    image_of_participant = models.ImageField(null=True, blank=True)
   
   #TODO da ga vezes sa filmom nekako

    def __str__(self):
        return self.name


class Title(models.Model):
    
    name = models.CharField(max_length=255)
    #participants = models.ForeignKey('Participant', on_delete=models.CASCADE)
    
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