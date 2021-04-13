from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Message(models.Model):
    created_date = models.DateTimeField(default=now, editable=False)
    users = models.ManyToManyField(User)
    text = models.CharField(max_length=256)