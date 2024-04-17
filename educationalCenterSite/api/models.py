from django.db import models

# Create your models here.
class UserAdmins(models.Model):
    idUsers = models.CharField(max_length=100)
    checkAdmin = models.CharField(max_length=100)

class UpdateEmployees(models.Model):
    idEmployees = models.CharField(max_length=100)
    fullName = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

class AddEmployees(models.Model):
    idEmployees = models.CharField(max_length=100)
    fullName = models.CharField(max_length=100)
    position = models.CharField(max_length=100)