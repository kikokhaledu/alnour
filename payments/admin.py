from django.contrib import admin
from django import forms
from .models import SupplierPayment

class SupplierPaymentAdminForm(forms.ModelForm):
    class Meta:
        model = SupplierPayment
        exclude = ['issued_by']

class SupplierPaymentAdmin(admin.ModelAdmin):
    form = SupplierPaymentAdminForm
    list_display = ('date', 'issued_by', 'paid_amount','supplier')
    list_filter = ('supplier__name', 'date', 'paid_amount', 'issued_by__email')
    search_fields = ('date', 'paid_amount')
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # if object has no primary key, it's being created
            obj.issued_by = request.user  # set issued_by to the current user
        super().save_model(request, obj, form, change)

admin.site.register(SupplierPayment, SupplierPaymentAdmin)
