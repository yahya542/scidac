
from django.urls import path
from myapp.views import   a,k, rlg,  sc, dac, school, buat, cu, todo_list, add_todo, toggle_complete, delete_todo, ubah_password, setting, make_yahya_admin, RegisterAPIView, loginAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
  
   
    path('-ubah_akun', ubah_password , name="ubah akun"),
    path('-setting', setting , name="setting"),


    #menengah       
    path('-aljabar', a, name='aljabar'),
    #tinggi
    path('-kalkulus', k, name='kalkulus'),
    
    path('-adm1', make_yahya_admin, name="adm1"),


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
    path('-cu', cu, name='cu'),

    ##keuangan 
    #api 
  
    path('/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Endpoint untuk me-refresh token JWT
    path('/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('/login', loginAPIView.as_view (), name='login'),
    path('/register', RegisterAPIView.as_view(), name='register'),




    

]

  

