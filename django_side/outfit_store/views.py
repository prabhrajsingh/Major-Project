from django.shortcuts import render
from .forms import outfit_upload_form
# Create your views here.
def menu(request):
    return render (request, 'Menu.html')

def OOTD(request):
    return render (request, 'OOTD.html')

def upload(request):
    context = {}
    context['form'] = outfit_upload_form()  
    return render (request, 'upload.html', context)

def wardrobe(request):
    return render (request, 'wardrobe.html')

def profile(request):
    return render (request, 'user.html')

def settings(request):
    return render (request, 'settings.html')