from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    task = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task


class fotoProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gambar_profile = models.ImageField(null=True, blank=True, upload_to='profile_pics/')

    def __str__(self):
        return  f"Foto Profil {self.user.username}"

