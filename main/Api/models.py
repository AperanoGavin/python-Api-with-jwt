from django.db import models
from django.contrib.auth.models  import User

# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=30)
    website= models.URLField(max_length=30)
    
    def __str__(self):
            return self.name
        
        
class Movie(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE  , related_name='user')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform , on_delete=models.CASCADE , related_name= "platform" )
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title

    