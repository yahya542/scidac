from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormLogin, FotoProfileForm, FormSignUp, BiodataForm
from django.contrib.auth import login, authenticate,  update_session_auth_hash
from django.contrib.auth.models import User
from .models import Todo,  Profile
from .forms import TodoForm, UbahPasswordForm
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import loginSerializer, RegisterSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request, *args, **kwargs):
        user = request.user  
        serializer = UserSerializer(user)  
        return Response(serializer.data)  







##auth
class RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Membuat pengguna baru
            return Response({'message': 'pengguna berhasil terdaftar!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class loginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = loginSerializer(data=request.data)

        if serializer.is_valid():
            # Mendapatkan objek user yang valid
            user = serializer.validated_data['user']
            # Membuat RefreshToken dan AccessToken untuk user
            refresh = RefreshToken.for_user(user)

            # Mengembalikan token access dan refresh dalam response
            return Response({
                'username': user.username,
                'access_token': str(refresh.access_token),  # Token akses
                'refresh_token': str(refresh),  # Token refresh
            }, status=status.HTTP_200_OK)

        # Mengembalikan error jika validasi gagal
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
def make_yahya_admin(request):
    yahya = User.objects.get(username='yahya')
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
    profile = request.user.safe_profile
    return render(request, 'dashboard.html', {'profile': profile})

    
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
    return render(request, "autentikasi/password_reset_form.html")
def akun(request): 
    return render(request, 'autentikasi/akun.html')
def setting(request): 
    return render(request, 'autentikasi/setting.html')

#edit profile
def edit_profile(request):
    profile = request.user.profile  # pastikan profile sudah ada, pakai get_or_create jika perlu
    if request.method == 'POST':
        form = FotoProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Foto profil berhasil diperbarui.')
            return redirect('dashboard')  # atau halaman lain yang diinginkan
        else:
            messages.error(request, 'Gagal menyimpan foto profil.')
    else:
        form = FotoProfileForm(instance=profile)

    return render(request, 'autentikasi/edit_profil.html', {'form': form})

#edit akun 
def edit_data(request):
    if not request.user.is_authenticated:
        return redirect('login')

    # Buat profile jika belum ada
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = BiodataForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('akun')  # ganti dengan nama url yang sesuai
    else:
        form = BiodataForm(instance=profile)

    return render(request, 'autentikasi/edit_data.html', {
        'form': form,
        'form_email': request.user.email,
        'profile': profile,
    })





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

from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import UbahPasswordForm

def ubah_password(request):
    form = UbahPasswordForm(request.user, request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            # Ambil data form
            old_password = form.cleaned_data.get('old_password')
            new_password = form.cleaned_data.get('new_password')
            confirm_password = form.cleaned_data.get('confirm_password')

            # Verifikasi apakah sandi lama sesuai
            if not request.user.check_password(old_password):
                messages.error(request, "Maaf, sandi lama Anda salah.")
                return render(request, 'autentikasi/ubah_sandi.html', {'form': form})
            
            # Verifikasi apakah password baru dan konfirmasi sama
            if new_password != confirm_password:
                messages.error(request, "Ubah kata sandi gagal. Konfirmasi password tidak sesuai.")
                return render(request, 'autentikasi/ubah_sandi.html', {'form': form})

            # Update password baru
            user = request.user
            user.set_password(new_password)
            user.save()

            # Update session agar user tetap login
            update_session_auth_hash(request, user)

            # Kirim pesan sukses
            messages.success(request, "Password Anda berhasil diubah. Silakan login kembali.")

            # Redirect ke halaman login
            return redirect('login')

        else:
            # Jika form tidak valid, beri pesan error
            messages.error(request, "Ada kesalahan dalam pengisian form.")
            return render(request, 'autentikasi/ubah_sandi.html', {'form': form})
    
    else:
        form = UbahPasswordForm(request.user)
    
    return render(request, 'autentikasi/ubah_sandi.html', {'form': form})












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







