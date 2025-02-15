from django.shortcuts import render

# Create your views here.
def keuangan (request): 
    return render (request, 'keuangan/tabungan.html')
