import os
from django.shortcuts import render



def capsule(request):
    return render(request, 'capsule/capsule.html')