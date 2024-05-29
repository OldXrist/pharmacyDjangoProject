from django.contrib.auth.models import User
from django.db import models


class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    about = models.TextField(blank=True)
    city = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.user.username
