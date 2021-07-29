from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here. models is a data base classes

# each class has its own table in database, on the class each line has its own table
# your class is the basis of your each data input in database
# run $ python manage.py makemigrations for changes
# and create a migrations file in migration directory
# then run $ python manage.py migrate to save any changes
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title