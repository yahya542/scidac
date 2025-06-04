
from django.urls import path
from myapp.views import   a,k, rlg,  sc,  ubah_password, setting, make_yahya_admin, RegisterAPIView, loginAPIView, UserAPIView
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

 
    #api 
  
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login', loginAPIView.as_view (), name='login'),
    path('register', RegisterAPIView.as_view(), name='register'), 
    path('user', UserAPIView.as_view(), name='user'),




    

]

  

