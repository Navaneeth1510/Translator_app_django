from django.db import models

class UserDetails(models.Model):
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
