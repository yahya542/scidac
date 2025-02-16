from django.urls import path
from mathapp.views import  persegi, segitiga, geometri, Ppanjang, Lingkaran, Bketupat, kubus,math, stat

urlpatterns = [
      ## math ##
    path('-math', math, name='math' ),
    #Dasar
    #geometri
    path('-geometri', geometri, name='geometri'),
    path('persegi/', persegi, name='persegi'),
    path('segitiga/', segitiga, name='segitiga'),
    path('Ppanjang/', Ppanjang, name='Ppanjang'),
    path('Lingkaran/', Lingkaran, name='Lingkaran'),
    path('Bketupat/', Bketupat, name='Bketupat'),
    path('kubus/', kubus, name='kubus'),
    #stat
    path('-stat/', stat, name='stat'),

]