from django.db import models

# Create your models here.
class UserAdmins(models.Model):
    idUsers = models.CharField(max_length=100)
    checkAdmin = models.CharField(max_length=100)