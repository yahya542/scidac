from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormLogin, FotoProfileForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import Todo, fotoProfile
from .forms import TodoForm
from django.http import HttpResponse




def make_yahya_admin(request):
    yahya = User.objects.get(username='Yahya')
    yahya.is_superuser = True
    yahya.is_staff = True
    yahya.save()
    return HttpResponse("Yahya telah diberikan akses admin.")










#menengah
def a(request): 
    return render (request, 'math/menengah/aljabar.html')
#tinggi
def k(request): 
    return render (request, 'math/tinggi/kalkulus.html')

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
def ubah(request): 
    return render (request, 'autentikasi/ubah_sandi.html')

def update_profile(request):
    try:
        foto_profile = fotoProfile.objects.get(user=request.user)
    except fotoProfile.DoesNotExist:
        foto_profile = None

    if request.method == 'POST':
        form = FotoProfileForm(request.POST, request.FILES, instance=foto_profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect ke halaman profil setelah upload
    else:
        form = FotoProfileForm(instance=foto_profile)

    return render(request, 'autentikasi/akun.html', {'form': form})


#dac 
def dac(request): 
    return render (request, 'dac/dac.html')
def buat(request): 
    return render (request, 'dac/add_todo.html')




def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'dac/dac.html', {'todos': todos})

def add_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'dac/add_todo.html', {'form': form})

def toggle_complete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')

def delete_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('todo_list')
















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

#edit-profile
def edit_profile (request) : 
    return render (request, 'autentikasi/edit_profil.html')

#edit akun 
def edit_data (request) : 
    return render (request, 'autentikasi/edit_data.html')

#keuangan 




