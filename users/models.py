from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 10)
    last_name = models.CharField(max_length = 10)
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    
