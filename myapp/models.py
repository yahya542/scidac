from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hp = models.CharField(max_length=15, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=(('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')), blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default.jpg')

    def __str__(self):
        return f" {self.user.username }'s profile"

