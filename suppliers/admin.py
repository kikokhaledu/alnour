from django.contrib import admin
from .models import Supplier, SupplierBatch
from django.db.models import Case, When, Value, IntegerField


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'shipping_total', 'total_provided_from_supplier', 'total_paid_to_supplier', 'pending_amount_to_the_supplier')
    list_filter = ('name',)
    search_fields = ('name',)
admin.site.register(Supplier, SupplierAdmin)




class SupplierBatchAdmin(admin.ModelAdmin):
    list_display = ('batch_date', 'shift', 'supplier', 'material_type', 'weight', 'price_per_ton', 'shipping', 'total')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            order_by_price_and_shipping=Case(
                When(price_per_ton__isnull=True, then=Value(0)),
                When(price_per_ton=0, then=Value(0)),
                When(shipping__isnull=True, then=Value(0)),
                When(shipping=0, then=Value(0)),
                default=Value(1),
                output_field=IntegerField(),
            )
        )
        return queryset.order_by('order_by_price_and_shipping')


admin.site.register(SupplierBatch,SupplierBatchAdmin)





