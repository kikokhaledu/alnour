from django.contrib import admin
from . models import raw_material,finished_products,batch
# Register your models here.
admin.site.register(raw_material)
admin.site.register(finished_products)
admin.site.register(batch)