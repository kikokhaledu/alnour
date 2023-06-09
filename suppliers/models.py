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
    shift = models.CharField(max_length=7)
    material_type = models.CharField(max_length=255, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    price_per_ton = models.FloatField(null=True, blank=True,default=0.0)
    shipping = models.FloatField(null=True, blank=True,default=0.0)
    total = models.FloatField(null=True, blank=True)
    
    def order_by_price_and_shipping(self):
        if self.price_per_ton is None or self.price_per_ton == 0 or self.shipping is None or self.shipping == 0:
            return 0
        else:
            return 1
    
    def __str__(self):
        return f"Supplier Batch: {self.batch_date} - for supplier: {self.supplier.name}"
    
