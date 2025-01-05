
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField(blank=True)
    dibuat_pada = models.DateTimeField(auto_now_add=True)
    tanggal_tenggat = models.DateTimeField(null=True, blank=True)
    selesai = models.BooleanField(default=False)
    pengguna = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.judul
