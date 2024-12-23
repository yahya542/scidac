
from django.urls import path
from myapp.views import  g, a,k


urlpatterns = [
    #Dasar
    path('-geometri', g, name='geometri'), 


    #menengah       
    path('-aljabar', a, name='aljabar'),


    #tinggi
    path('-kalkulus', k, name='kalkulus')

]