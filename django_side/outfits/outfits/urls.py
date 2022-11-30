"""outfits URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'BACKEND'
admin.site.site_title = 'BACKEND PANEL'
admin.site.index_title = 'WELCOME TO THE MANAGE PANEL'

from accounts.views import (
    login_view,
    logout_view,
    register_view, 
)
from . import views

from outfit_store.views import(
    menu,
    OOTD,
    dress_image_view,
    display_dress_images,
    profile,
    category,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('Menu', menu, name='Menu.html'),
    path('OOTD', OOTD, name='OOTD.html'),
    path('user', profile, name='user.html'),
    path('category', category, name='category.html'),
    path('upload', dress_image_view, name = 'upload.html'),
    path('wardrobe', display_dress_images, name='wardrobe.html'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
