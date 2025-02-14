from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormLogin, FotoProfileForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import Todo, fotoProfile
from .forms import TodoForm, PersegiForm, SegitigaForm, PpanjangForm , LingkaranForm, BketupatForm, kubusForm, statForm
import numpy as np





#=======math=====# 
def math(request): 
    return render (request, 'math/math.html')
#=dasar=#
def geometri(request) : 
    return render (request, 'math/dasar/geometri.html' )
#bangun datar
def persegi(request):
    if request.method == 'POST':
        form = PersegiForm(request.POST)
        if form.is_valid():
            sisi = form.cleaned_data['panjang']
            luas = sisi ** 2
            keliling = 4 * sisi 
            return render(request, 'math/dasar/hitung.html', {'form': form, 'luas': luas, 'bentuk': 'Persegi' , 'keliling' : keliling})
    else:
        form = PersegiForm()

    return render(request, 'math/dasar/hitung.html', {'form': form, 'bentuk': 'Persegi'})

def segitiga(request):
    if request.method == 'POST':
        form = SegitigaForm(request.POST)
        if form.is_valid():
            alas = form.cleaned_data['alas']
            tinggi = form.cleaned_data['tinggi']
            sisi_a = form.cleaned_data['sisi_a']
            sisi_b = form.cleaned_data['sisi_b']
            sisi_c = form.cleaned_data['sisi_c']
            luas = 0.5 * alas * tinggi
            keliling = sisi_a + sisi_b + sisi_c
          
            return render(request, 'math/dasar/hitung.html', {'form': form, 'luas': luas, 'keliling' : keliling,  'bentuk': 'Segitiga'})
    else:
        form = SegitigaForm()

    return render(request, 'math/dasar/hitung.html', {'form': form, 'bentuk': 'Segitiga'})

def Ppanjang(request):
    if request.method == 'POST':
        form = PpanjangForm(request.POST)
        if form.is_valid():
            panjang = form.cleaned_data['panjang']
            lebar = form.cleaned_data['lebar']
            luas = panjang * lebar 
            keliling = 2 * (panjang + lebar)
            return render(request, 'math/dasar/hitung.html', {'form': form, 'luas': luas, 'bentuk': 'Persegi Panjang', 'keliling' : keliling})
    else:
        form = PpanjangForm()

    return render(request, 'math/dasar/hitung.html', {'form': form, 'bentuk': 'Persegi Panjang'})

def Lingkaran(request):
    if request.method == 'POST':
        form = LingkaranForm(request.POST)
        if form.is_valid():
            jari_jari = form.cleaned_data['jari_jari']
            luas = 3.14159 * jari_jari * jari_jari
            keliling = 2 * 3.14159 * jari_jari
            return render(request, 'math/dasar/hitung.html', {'form': form, 'luas': luas, 'bentuk': 'Lingkaran', 'keliling' : keliling})
    else:
        form = LingkaranForm()

    return render(request, 'math/dasar/hitung.html', {'form': form, 'bentuk': 'Lingkaran'})

def Bketupat(request):
    if request.method == 'POST':
        form = BketupatForm(request.POST)
        if form.is_valid():
            d1 = form.cleaned_data['d1']
            d2 = form.cleaned_data['d2']
            sisi = form.cleaned_data['sisi']
            luas = (d1*d2) /2 
            keliling = 4 * sisi
            return render(request, 'math/dasar/hitung.html', {'form': form, 'luas': luas, 'bentuk': 'Lingkaran', 'keliling' : keliling})
    else:
        form = BketupatForm()

    return render(request, 'math/dasar/hitung.html', {'form': form, 'bentuk': 'Belah Ketupat'})

#bangun ruang 
def kubus(request):
    if request.method == 'POST':
        form = kubusForm(request.POST)
        if form.is_valid():
            sisi = form.cleaned_data['sisi']
            volume = np.power(sisi, 3)
            lp = 6 * (np.power(sisi, 2))
        
            return render(request, 'math/dasar/hitung.html', {'form': form, 'volume': volume, "lp" : lp})
    else:
        form = kubusForm()

    return render(request, 'math/dasar/hitung.html', {'form': form, 'bentuk': 'Kubus'})


## === stat ===#

    
# perhitungan/views.py




def stat(request):
    result = None
    if request.method == 'POST':
        form = statForm(request.POST)
        if form.is_valid():
            # Ambil data dari form dan ubah jadi list angka
            raw_data = form.cleaned_data['data']
            try:
                # Ubah string data menjadi list angka
                data = np.array([float(x.strip()) for x in raw_data.split(',') if x.strip()])  # Konversi ke array NumPy dan tangani spasi
                if len(data) == 0:
                    raise ValueError("Data tidak boleh kosong.")
                
                # Hitung statistik dasar menggunakan NumPy
                values, counts = np.unique(data, return_counts=True)
                
                # Hitung modus
                max_count = np.max(counts)
                modes = values[counts == max_count]

                # Jika hanya ada satu modus, ambil yang pertama
                modus = modes[0] if len(modes) == 1 else modes.tolist()

                mean = np.mean(data)
                median = np.median(data)
                stdev = np.std(data)  # Standar deviasi

                result = {
                    'mean': mean,
                    'median': median,
                    'modus': modus, 
                    'stdev': stdev,
                    'data': data.tolist()  # Convert kembali ke list untuk ditampilkan di template
                }
            except ValueError as e:
                result = {'error': f'Data yang dimasukkan tidak valid. Pastikan hanya angka yang dipisahkan koma. ({str(e)})'}
        else:
            result = {'error': 'Form tidak valid.'}
    else:
        form = statForm()

    return render(request, 'math/dasar/hitung.html', {'form': form, 'result': result})









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
def keuangan (request): 
    return render (request, 'keuangan/tabungan.html')




