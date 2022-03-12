from django.contrib import admin
from . models import PO_table,invoices_table,expenses_category ,expenses,loader_expenses



admin.site.register(PO_table)
admin.site.register(invoices_table)
admin.site.register(expenses_category)
admin.site.register(expenses)
admin.site.register(loader_expenses)