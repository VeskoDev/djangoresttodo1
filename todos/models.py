from django.db import models
from helpers.models import TrackingModel





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

class Participant(models.Model):
    
    name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    date_of_birth= models.DateField(blank=True, null=True)  
    description= models.TextField(blank=True, null=True)
    image_of_participant= models.ImageField(null=True, blank=True)
    Movie = models.ManyToManyField('Movie',blank=True)
    
    

    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=255)
    Movie = models.ManyToManyField('Movie', blank=True)

    def __str__(self):
        return self.name


class Movie(models.Model):

    title = models.CharField(max_length=255)
    featured_image = models.ImageField(null=True, blank=True)
    image_of_movie = models.ImageField(null=True, blank=True)
    video_of_movie = models.FileField(null=True, blank=True)
    description = models.TextField(blank=True)
    actors = models.ManyToManyField('Participant', through= Participant.Movie.through , null=True, blank=True)
    date_of_release = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    Tag = models.ManyToManyField('Tag', through=Tag.Movie.through , null=True, blank=True)

    def __str__(self):
        return self.title





class Title(models.Model):
    
    name = models.CharField(max_length=255)
    #participants = models.ForeignKey('Participant', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
