from django import forms
from django.contrib.auth.models import User 
from .models import Todo, fotoProfle





####math 
#Geometri 
#persegi 
class PersegiForm(forms.Form):
    panjang = forms.FloatField(label='Panjang Sisi', min_value=0)
#pp
class PpanjangForm(forms.Form):
    panjang = forms.FloatField(label='Panjang', min_value=0)
    lebar = forms.FloatField(label='Lebar', min_value=0) 
#segitiga
class SegitigaForm(forms.Form):
    alas = forms.FloatField(label='Alas', min_value=0)
    tinggi = forms.FloatField(label='Tinggi', min_value=0)
    sisi_a = forms.FloatField(label='Sisi A', min_value=0)
    sisi_b = forms.FloatField(label='Sisi B', min_value=0)
    sisi_c = forms.FloatField(label='Sisi C', min_value=0)
#Lingkaran 
class LingkaranForm(forms.Form):
    jari_jari = forms.FloatField(label='Jari-jari', min_value=0)
#ketupat
class BketupatForm(forms.Form):
    d1 = forms.FloatField(label='Diagonal 1 ', min_value=0)
    d2 = forms.FloatField(label='Diagonal 2', min_value=0)
    sisi = forms.FloatField(label='Sisi', min_value=0)

#kubus 
class kubusForm(forms.Form): 
    sisi = forms.FloatField(label='Sisi', min_value=0)


##statistika dasar ##
class statForm(forms.Form):
    data = forms.CharField(widget=forms.Textarea, help_text="Masukkan angka yang dipisahkan dengan koma (misal: 1,2,3,4,5)")


##### authentication
class FormLogin(forms.Form):
    username = forms.CharField (
        widget= forms.TextInput (attrs={'class' : 'form-control', 'type':'text'}), 
    )
    password = forms.CharField (
        widget= forms.PasswordInput (attrs={'class' : 'form-control'}),
    )

from django import forms

class FormSignUp(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}), #test 12334
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    # Validasi konfirmasi password
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password') #oke gas
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Password dan konfirmasi password tidak cocok.")
        return cleaned_data
    

#profile
class fotoProfileForm(forms.ModelForm): 
    class Meta: 
        model : fotoProfle
        fields : ['gambar_profile']





#todo
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task']
        widgets = {
            'task': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tulis tugas baru...'}),
        }


    



    