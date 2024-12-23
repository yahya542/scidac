# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('-jadwal', views.jadwal, name='jadwal'),         # Halaman daftar jadwal
    path('-buat', views.buat, name='buat'),               # Halaman buat jadwal baruh
    path('-lihat/<int:jadwal_id>', views.lihat, name='lihat'),  # Halaman lihat detail jadwal
]
