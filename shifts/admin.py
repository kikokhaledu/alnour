from django.contrib import admin
from . models import shift_types_table,shift_reports
from products.models import products_table
# Register your models here.


admin.site.register(shift_types_table)


# class products_tableInline(admin.StackedInline):
#     model = products_table
#     extra = 1  

# @admin.register(shift_reports)
# class shift_reportsAdmin(admin.ModelAdmin):
#     inlines = [products_tableInline]
#     show_change_link = True
#     # list_display = ('hotel', 'title',)
#     # extra = 1
#     # list_filter = ('listing_type',)