from django.db import models



class Supplier(models.Model):
    name = models.CharField(max_length=255)
    total_paid_to_supplier = models.FloatField(null=True, blank=True)
    shipping_total = models.FloatField(null=True, blank=True)
    total_provided_from_supplier = models.FloatField(null=True, blank=True)
    pending_amount_to_the_supplier = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.name


class SupplierBatch(models.Model): #added when a record 
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    batch_date = models.DateField(auto_now_add=True)
    material_type = models.CharField(max_length=255, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    price_per_ton = models.FloatField(null=True, blank=True)
    shipping = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Supplier Batch: {self.batch_date} - for supplier: {self.supplier.name}"
    
