from django.contrib import admin
from django.urls import path, include
from myapp.views import dashboard, my_login, signup_view, google, fb, forgot, akun, edit_profile, edit_data, FotoProfileForm , make_yahya_admin
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    ##auth
    path('admin/', admin.site.urls),
    path("dashboard",dashboard, name="dashboard"),
    path('', my_login, name="login"),
    path("google",google, name="google"),
    path("fb",fb, name="facebook"),
    path("signup", signup_view, name="signup"),
    path("forgot",forgot, name="forgot"),
    path("akun",akun, name="akun"),
    path("edit_profile", edit_profile, name="edit_profile"),
    path("edit_data", edit_data, name="edit_data"),
    path("userAdmin", make_yahya_admin , name="userAdmin"), 



    ##math
    path('study/', include('study.urls')),

    ##religi
    path('religi', include('myapp.urls')),

    ##religi
    path('science', include('myapp.urls')),

    ##school
    path('school', include('myapp.urls')),

    ##dac
    path('dac', include('myapp.urls')),

    #contact
    path('cu', include('myapp.urls')),

    #keuangan 
    path('mo', include('tabunganapp.urls')),

    path('auth', include('myapp.urls')),

    path('adm', include('myapp.urls')),
    path('api/', include('myapp.urls')),

  
]  

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



