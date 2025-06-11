from django.shortcuts import render
from .forms import PersegiForm, SegitigaForm, PpanjangForm , LingkaranForm, BketupatForm, kubusForm, statForm, AkarForm
import numpy as np

# Create your views here.
#=======math=====# 
def math(request): 
    return render (request, 'math/math.html')
#=dasar=#
def geometri(request) : 
    return render (request, 'math/dasar/geometri.html' )
def akarpangkat(request) : 
    return render (request, 'math/menengah/akarpangkat.html' )


#bangun datar
def persegi(request):
    if request.method == 'POST':
        form = PersegiForm(request.POST)
        if form.is_valid():
            sisi = form.cleaned_data['panjang']
            luas = sisi ** 2
            keliling = 4 * sisi 
            return render(request, 'math/hitung.html', {'form': form, 'luas': luas, 'bentuk': 'Persegi' , 'keliling' : keliling})
    else:
        form = PersegiForm()

    return render(request, 'math/hitung.html', {'form': form, 'bentuk': 'Persegi'})

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
          
            return render(request, 'math/hitung.html',  {'form': form, 'luas': luas, 'keliling' : keliling,  'bentuk': 'Segitiga', })
    else:
        form = SegitigaForm()

    return render(request, 'math/hitung.html', {'form': form, 'bentuk': 'Segitiga'})

def Ppanjang(request):
    if request.method == 'POST':
        form = PpanjangForm(request.POST)
        if form.is_valid():
            panjang = form.cleaned_data['panjang']
            lebar = form.cleaned_data['lebar']
            luas = panjang * lebar 
            keliling = 2 * (panjang + lebar)
            return render(request, 'math/hitung.html', {'form': form, 'luas': luas, 'bentuk': 'Persegi Panjang', 'keliling' : keliling})
    else:
        form = PpanjangForm()

    return render(request, 'math/hitung.html', {'form': form, 'bentuk': 'Persegi Panjang'})

def Lingkaran(request):
    if request.method == 'POST':
        form = LingkaranForm(request.POST)
        if form.is_valid():
            jari_jari = form.cleaned_data['jari_jari']
            luas = 3.14159 * jari_jari * jari_jari
            keliling = 2 * 3.14159 * jari_jari
            return render(request, 'math/hitung.html', {'form': form, 'luas': luas, 'bentuk': 'Lingkaran', 'keliling' : keliling})
    else:
        form = LingkaranForm()

    return render(request, 'math/hitung.html', {'form': form, 'bentuk': 'Lingkaran'})

def Bketupat(request):
    if request.method == 'POST':
        form = BketupatForm(request.POST)
        if form.is_valid():
            d1 = form.cleaned_data['d1']
            d2 = form.cleaned_data['d2']
            sisi = form.cleaned_data['sisi']
            luas = (d1*d2) /2 
            keliling = 4 * sisi
            return render(request, 'math/hitung.html', {'form': form, 'luas': luas, 'bentuk': 'Lingkaran', 'keliling' : keliling})
    else:
        form = BketupatForm()

    return render(request, 'math/hitung.html', {'form': form, 'bentuk': 'Belah Ketupat'})

#bangun ruang 
def kubus(request):
    rumusnya = None
    if request.method == 'POST':
        form = kubusForm(request.POST)
        if form.is_valid():
            sisi = form.cleaned_data['sisi']
            volume = np.power(sisi, 3)
            lp = 6 * (np.power(sisi, 2))
            rumusnya = f"volume = sisi^3  || luas permukaan = 6*sisi^2"
            return render(request, 'math/hitung.html', {'form': form, 'volume': volume, "lp" : lp, 'rumusnya':rumusnya})
    else:
        form = kubusForm()

    return render(request, 'math/hitung.html', {'form': form, 'bentuk': 'Kubus' })

def stat(request):
    result = None
    rumus = None
    if request.method == 'POST':
        form = statForm(request.POST)
        if form.is_valid():
            raw_data = form.cleaned_data['data']
            try:
                data = np.array([float(x.strip()) for x in raw_data.split(',') if x.strip()])   
                if len(data) == 0:
                    raise ValueError("Data tidak boleh kosong.")
                values, counts = np.unique(data, return_counts=True)
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
                rumus =  "rata-rata = banyaknya data dibagi banyaknya anggota"
            except ValueError as e:
                result = {'error': f'Data yang dimasukkan tidak valid. Pastikan hanya angka yang dipisahkan koma. ({str(e)})'}
        else:
            result = {'error': 'Form tidak valid.'}
    else:
        form = statForm()

    return render(request, 'math/hitung.html', {'form': form, 'result': result, 'rumus_stat': rumus})

def akar(request):
    rumusakar = None
    if request.method == 'POST':
        form = AkarForm(request.POST)
        if form.is_valid():
            akar = form.cleaned_data['akar']
            nilai = form.cleaned_data['nilai']
            hasil = np.power(nilai, 1/akar)
            rumusakar = 'n^a = n x sebanyak a'
            return render(request, 'math/hitung.html', {'form': form, 'hasil':hasil, 'rumusnya':rumusakar})
    else:
        form = AkarForm()

    return render(request, 'math/hitung.html', {'form': form, 'bentuk': 'akar' })
