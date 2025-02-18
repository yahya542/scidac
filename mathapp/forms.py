from django import forms
from django.contrib.auth.models import User 


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
    data = forms.CharField(widget=forms.Textarea, help_text= f"<br> Masukkan angka yang dipisahkan dengan koma (misal: 1,2,3,4,5)")

class AkarForm(forms.Form): 
    akar = forms.FloatField(label='Akar', min_value=0)
    nilai = forms.FloatField(label='Nilai', min_value=0)
