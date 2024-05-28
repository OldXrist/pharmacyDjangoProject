from django.contrib.auth.models import User
from django.db import models


class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    about = models.TextField()
    city = models.CharField(max_length=30)
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
