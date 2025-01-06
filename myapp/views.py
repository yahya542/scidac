from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import FormLogin
from django.contrib.auth.models import User



#science 
def sc (request): 
    return render (request, 'science/science.html')


#religi 
def rlg(request) : 
    return render (request, 'religi/religi.html')


# auth 
def dashboard(request): 
    return render(request, 'dashboard.html', {'user': request.user})
def register(request): 
     return render(request, 'register.html' )
def submit_data(request): 
    return render(request, "submit.html")
def success(request): 
    return render(request, 'aunt_succes.html')
def google(request): 
    return render(request, 'autentikasi/google.html')
def fb(request): 
    return render(request, 'autentikasi/facebook.html')
def forgot(request): 
    return render(request, "autentikasi/forgot-password.html")
def akun(request): 
    return render(request, 'autentikasi/akun.html')


#math 
def math(request): 
    return render (request, 'math/math.html')
#dasar
def g(request): 
    return render (request, 'math/dasar/geometri.html')
#menengah
def a(request): 
    return render (request, 'math/menengah/aljabar.html')
#tinggi
def k(request): 
    return render (request, 'math/tinggi/kalkulus.html')


#dac 
def dac(request): 
    return render (request, 'dac/dac.html')
def buat(request): 
    return render (request, 'dac/buat_todo.html')

#school 
def school(request): 
    return render (request, 'school/school.html')

#contact us 
def cu (request): 
    return render (request, 'contact/contact_us.html')



#auth
def my_login(request): 
    form = FormLogin()
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None :
                login(request, user)
                return redirect ('dashboard')
            else:  # Jika username atau password salah
                messages.error(request, 'Maaf, username atau password anda salah.')

    return render(request,  'autentikasi/login.html', {'form':form})

from django.shortcuts import render, redirect
from .forms import FormSignUp

def signup_view(request):
    if request.method == 'POST':
        form = FormSignUp(request.POST)
        if form.is_valid():
           
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')  # Arahkan ke halaman login setelah berhasil sign up
    else:
        form = FormSignUp()

    return render(request, 'autentikasi/register.html', {'form': form})






