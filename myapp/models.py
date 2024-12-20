from django.db import models

class Jadwal(models.Model):
    nama_pelajaran = models.CharField(max_length=100,null=True, blank=True)
    hari = models.CharField(max_length=20, null=True, blank=True)
    jam_mulai = models.TimeField(default='00:00:00')
    jam_selesai = models.TimeField(default='01:00:00')

    def __str__(self):
        return f"{self.nama_pelajaran} - {self.hari}"
