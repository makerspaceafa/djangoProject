from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=60)
    #hierar = models.IntegerField(max_length=2)

    # on_delete -> CASCADE para se apagarem o user, tb se apagarem as tasks
    user = models.ForeignKey(User, on_delete=models.CASCADE)
