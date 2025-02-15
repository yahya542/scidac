from django.urls import path
from tabunganapp.views import  keuangan

urlpatterns = [
path('-tabungan', keuangan, name='tabungan'),
]