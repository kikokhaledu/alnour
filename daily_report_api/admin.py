from django.contrib import admin
from .models import Configuration, MeasurementUnit, DailyReport, ProductionRecord, RawMaterialRecord, SoldProductRecord

class ProductionRecordInline(admin.StackedInline):
    model = ProductionRecord
    extra = 1  # Display one extra form

class RawMaterialRecordInline(admin.StackedInline):
    model = RawMaterialRecord
    extra = 1  # Display one extra form
    
class SoldProductRecordInline(admin.StackedInline):
    model = SoldProductRecord
    extra = 1  # Display one extra form
    
class DailyReportAdmin(admin.ModelAdmin):
    list_display = ('day', 'shift')
    inlines = [ProductionRecordInline, RawMaterialRecordInline, SoldProductRecordInline]

admin.site.register(Configuration)
admin.site.register(MeasurementUnit)
admin.site.register(DailyReport, DailyReportAdmin)
