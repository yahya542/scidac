from django import forms
from .models import Jadwal
from django.contrib.auth.models import User 


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
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    # Validasi konfirmasi password
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Password dan konfirmasi password tidak cocok.")
        return cleaned_data



#### jadwal
class JadwalForm(forms.ModelForm):
    class Meta:
        model = Jadwal
        fields = ['nama_pelajaran', 'hari', 'jam_mulai', 'jam_selesai']  # Pastikan field sesuai dengan model
