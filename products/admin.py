from django.contrib import admin
from .models import product_units,products_table

admin.site.register(product_units)
admin.site.register(products_table)


admin.site.site_header = "AlNour Rubber"
admin.site.site_title = "AlNour Rubber"
admin.site.index_title = "Below are your allowed panels"