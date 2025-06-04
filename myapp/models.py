from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class Todo(models.Model):
    task = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hp = models.CharField(max_length=15, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=(('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')), blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default.jpg')
    nama_lengkap = models.CharField(max_length=100, blank=True, null=True)
    points = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f" {self.user.username }'s profile"
def get_or_create_profile(self):
    profile, created = Profile.objects.get_or_create(user=self)
    return profile

User.add_to_class('safe_profile', property(get_or_create_profile))

