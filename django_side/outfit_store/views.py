from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
  

# Create your views here.
def menu(request):
    return render (request, 'Menu.html')

def OOTD(request):
    return render (request, 'OOTD.html')

def dress_image_view(request):
    if request.method == 'POST':
        form = DressForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/Menu')
    else:
        form = DressForm()
    return render(request, 'upload.html', {'form' : form})
  
def display_dress_images(request):
  
    if request.method == 'GET':
        # getting all the objects of dress.
        Dress = outfit_upload.objects.all() 
        return render(request, 'wardrobe.html',{'dress_images' : Dress})


def profile(request):
    return render (request, 'user.html')

def category(request):
    return render (request, 'category.html')