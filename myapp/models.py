from django.db import models

# Create your models here.
class UserInterface(models.Model):
    UserName=models.CharField(max_length=200)
    UserEmail=models.EmailField()
    UserPassword=models.CharField(max_length=100)
    UserPhone=models.CharField(max_length=11)

#Create your models here.
class Image(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=250)
    Image=models.ImageField(upload_to='Images/')
