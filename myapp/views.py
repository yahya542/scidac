from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .models import  Jadwal
from .forms import FormLogin, JadwalForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




# Create your views here.
def dashboard(request): 
    return render(request, 'dashboard.html', {'user': request.user})
def register(request): 
     return render(request, 'register.html' )
def submit_data(request): 
    return render(request, "submit.html")
def success(request): 
    return render('aunt_succes.html')

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






####### jadwal #########

# View untuk menampilkan daftar jadwal
def jadwal(request):
    jadwals = Jadwal.objects.all()  # Ambil semua data jadwal dari database
    return render(request, 'jadwal/jadwal.html', {'jadwal': jadwal})

# View untuk membuat jadwal baru
def buat(request):
    if request.method == 'POST':
        form = Jadwal.objects.all(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = JadwalForm()
    return render(request, 'jadwal/buat.html', {'form': form})

# View untuk melihat detail jadwal
def lihat(request, jadwal_id):
    try:
        jadwal = Jadwal.objects.get(id=jadwal_id)  # Ambil jadwal berdasarkan ID
    except Jadwal.DoesNotExist:
        return HttpResponse("Jadwal tidak ditemukan", status=404)
    return render(request, 'jadwal/lihat.html', {'jadwal': jadwal})