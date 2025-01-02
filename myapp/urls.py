
from django.urls import path
from myapp.views import  g, a,k, rlg, math, sc, dac, school


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

    ###school
    #school 
    path('-school', school, name='school' )

    

]

  

