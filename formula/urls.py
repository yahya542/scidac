from django.urls import path
from formula.math_view import persegi, segitiga, geometri, Ppanjang, Lingkaran, Bketupat, kubus, math, stat, akarpangkat, akar


urlpatterns = [

    path('math/', math, name='math'),
    path('geometri/', geometri, name='geometri'),
    path('persegi/', persegi, name='persegi'),
    path('segitiga/', segitiga, name='segitiga'), 
    path('Ppanjang/', Ppanjang, name='Ppanjang'),
    path('Lingkaran/', Lingkaran, name='Lingkaran'),
    path('Bketupat/', Bketupat, name='Bketupat'),
    path('kubus/', kubus, name='kubus'),
    path('stat/', stat, name='stat'),
    path('akarpangkat/', akarpangkat, name='akarpangkat'),
    path('akar/', akar, name='akar'),
]
