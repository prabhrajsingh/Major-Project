from django.contrib import admin
from outfit_store.models import store
# Register your models here.
class outfit_admin(admin.ModelAdmin):
    list_display = ['Id', 'User_name', 'Timestamp', 'Updated']
    search_fields = ['Id']

admin.site.register(store, outfit_admin)