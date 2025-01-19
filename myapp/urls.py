
from django.urls import path
from myapp.views import   a,k, rlg, math, sc, dac, school, buat, cu, todo_list, add_todo, toggle_complete, delete_todo, geometri


urlpatterns = [
    ## math ##
    path('-math', math, name='math' ),
    #Dasar
   
    path('-geometri', geometri, name='geometri'),
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
     path('-lihat',todo_list, name='todo_list'),
    path('-tambah/', add_todo, name='add_todo'),
    path('toggle_complete/<int:pk>/',toggle_complete, name='toggle_complete'),
    path('delete/<int:pk>/',delete_todo, name='delete_todo'),

    ###school
    #school 
    path('-school', school, name='school' ),

    ####contact 
    path('-cu', cu, name='cu')

    

]

  

