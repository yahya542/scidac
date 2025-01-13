from django import forms
from django.contrib.auth.models import User 
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['no_hp', 'alamat']


####math 
#Geometri 


# Form untuk Persegi
class PersegiForm(forms.Form):
    sisi = forms.FloatField(label='Masukkan sisi Persegi', min_value=0)

# Form untuk Lingkaran
class LingkaranForm(forms.Form):
    jari_jari = forms.FloatField(label='Masukkan jari-jari Lingkaran', min_value=0)

# Form untuk Segitiga
class SegitigaForm(forms.Form):
    alas = forms.FloatField(label='Masukkan alas Segitiga', min_value=0)
    tinggi = forms.FloatField(label='Masukkan tinggi Segitiga', min_value=0)





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



    