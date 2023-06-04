from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Client, ClientAdmin)
