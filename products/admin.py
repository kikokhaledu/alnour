from django.contrib import admin
from .models import ProductType, material_type

class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)

admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(material_type)
