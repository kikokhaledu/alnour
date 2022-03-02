from django.contrib import admin
from . models import PO_table,invoices_table



admin.site.register(PO_table)
admin.site.register(invoices_table)