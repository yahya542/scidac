from django import forms
from django.contrib.auth.models import User 
from .models import Todo, Persegi, PersegiPanjang




####math 
#Geometri 


# Form untuk Persegi
class PersegiForm(forms.ModelForm):
    class Meta:
        model = Persegi
        fields = ['sisi']
# Form untuk Lingkaran

    

# Form untuk Segitiga
class PersegiPanjangForm(forms.ModelForm):
    panjang = forms.FloatField(label='panjang', min_value=0)
    lebar = forms.FloatField(label='lebar', min_value=0)

class PersegiPanjangForm(forms.ModelForm):
    class Meta:
        model = PersegiPanjang
        fields = ['panjang', 'lebar']



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
    
#todo



class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task']
        widgets = {
            'task': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tulis tugas baru...'}),
        }


    



    