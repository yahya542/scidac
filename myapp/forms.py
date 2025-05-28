from django import forms
from django.contrib.auth.models import User 
from .models import Todo, Profile
from django.contrib.auth.forms import PasswordChangeForm











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
    
#ubah password 
class UbahPasswordForm(PasswordChangeForm): 
    class Meta: 
        model = User 
        fields = ['old_password', 'new_password1', 'new_password2' ]











#todo
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task']
        widgets = {
            'task': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tulis tugas baru...'}),
        }

#fotoprofile


class FotoProfileForm(forms.ModelForm):
    class Meta:
        model = Profile  
        fields = ['profile_picture'] 
        
#biodata
class BiodataForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nama_lengkap', 'alamat', 'gender', 'hp']
        widgets = {
            'nama_lengkap': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'hp': forms.TextInput(attrs={'class': 'form-control'}),
        } 

    