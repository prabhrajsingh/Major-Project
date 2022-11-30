from django.contrib import admin
# from outfit_store.models import store
from outfit_store.models import outfit_upload

# Register your models here.

class outfit_upload_admin(admin.ModelAdmin):
    list_display = ['User_name', 'dress_name', 'Timestamp', 'Updated']
    search_fields = ['dress_name', 'User_name']

# class outfit_admin(admin.ModelAdmin):
#     list_display = ['Id', 'User_name', 'Timestamp', 'Updated']
#     search_fields = ['Id']

admin.site.register(outfit_upload, outfit_upload_admin)

