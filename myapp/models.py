from django.db import models
import numpy as np

class Persegi(models.Model):
    sisi = models.FloatField()  # Field untuk sisi persegi
    
    def hitung_luas(self):
        # Menggunakan NumPy untuk menghitung luas persegi
        return np.square(self.sisi)  # Luas = sisi^2


class Todo(models.Model):
    task = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task




