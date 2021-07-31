from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# CASCADE means if the user is deleted profile is deleted but if profile is deleted users
# is not deleted


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
