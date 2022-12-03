from django.db import models

# Create your models here.
class Feuture(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField("themes-pixeden icon",max_length=50)
    def __str__(self):
        return self.name
    
class ScreenShot(models.Model):
    name=models.CharField(max_length=100)
    screen = models.ImageField(upload_to="screenshots")
    def __str__(self):
        return self.name

class FeedBack(models.Model):
    feedback = models.CharField(max_length=80)
    client = models.CharField(max_length=100)
    image_client = models.ImageField(upload_to="feedback_client")
    description = models.TextField()
    post = models.CharField(max_length=50)

    def __str__(self):
        return self.client
