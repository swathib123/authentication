from django.db import models

# Create your models here.
class Authenication(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class SupervisorAuthenication(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)    
