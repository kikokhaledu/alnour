from django.contrib import admin
from .models import Supplier, SupplierBatch

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'shipping_total', 'total_provided_from_supplier', 'total_paid_to_supplier', 'pending_amount_to_the_supplier')
    list_filter = ('name',)
    search_fields = ('name',)
admin.site.register(Supplier, SupplierAdmin)

class SupplierBatchAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'material_type', 'weight', 'price_per_ton', 'shipping')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.level == 'owner':
            return qs
        return qs.exclude(price_per_ton__in=[0, None]).exclude(shipping__in=[0, None])

    def owner_view(self, request):
        if request.user.level == 'owner':
            return SupplierBatch.objects.filter(price_per_ton__in=[0, None], shipping__in=[0, None])
        return SupplierBatch.objects.none()

    owner_view.short_description = 'Owner View'
    owner_view.allow_tags = True

    list_filter = ('supplier', 'material_type', 'weight', 'price_per_ton', 'shipping')


class SupplierBatchProxy(SupplierBatch):
    class Meta:
        proxy = True
        verbose_name = 'Supplier Batch needs info'
        verbose_name_plural = 'Supplier Batches need info'
        
class SupplierBatchProxyAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'material_type', 'weight', 'price_per_ton', 'shipping')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(price_per_ton__in=[0, None], shipping__in=[0, None])

admin.site.register(SupplierBatchProxy, SupplierBatchProxyAdmin)


admin.site.register(SupplierBatch,SupplierBatchAdmin)





