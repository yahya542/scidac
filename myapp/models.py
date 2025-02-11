from django.db import models
import numpy as np
from django.contrib.auth.models import User


class Todo(models.Model):
    task = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task


class fotoProfle(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gambar_profile = models.ImageField(upload_to='media/', default='static/img/undraw_profile.svg')

    def __str__(self):
        return self.user.username

