
from django.contrib import admin
from django.urls import path, include
from myapp.views import dashboard, my_login, signup_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path("dashboard",dashboard, name="dashboard"),
    path('jadwal', include('myapp.urls'), name="jadwal"),
    path('', my_login, name="login"),
    path("signup", signup_view, name="signup")
  
]  


