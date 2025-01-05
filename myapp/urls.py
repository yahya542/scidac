
from django.urls import path
from myapp.views import  g, a,k, rlg, math, sc, dac, school, buat


urlpatterns = [
    ## math ##
    path('-math', math, name='math' ),
    #Dasar
    path('-geometri', g, name='geometri'), 
    #menengah       
    path('-aljabar', a, name='aljabar'),
    #tinggi
    path('-kalkulus', k, name='kalkulus'),


    ## religi ##
    #dashboard 
    path('-rlg', rlg, name='religi'),


    ###science 
    #dashboard 
    path('-sc', sc , name='science' ),

    ####dac 
    #dashboard 
    path('-dac', dac , name='dac' ),
    path('-buat', buat , name='buat'),

    ###school
    #school 
    path('-school', school, name='school' )

    

]

  

