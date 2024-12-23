
from django.contrib import admin
from django.urls import path, include
from myapp.views import dashboard, my_login, signup_view, google, fb, forgot


urlpatterns = [
    path('admin/', admin.site.urls),
    path("dashboard",dashboard, name="dashboard"),
    path('', my_login, name="login"),
    path("google",google, name="google"),
    path("fb",fb, name="facebook"),
    path("signup", signup_view, name="signup"),
    path("forgot",forgot, name="forgot"),
    path('math', include('myapp.urls')),

  
]  


