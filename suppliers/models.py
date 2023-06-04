from django.db import models
from daily_report_api.models import RawMaterialRecord
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver



class Supplier(models.Model):
    name = models.CharField(max_length=255)
    shipping_total = models.FloatField(null=True, blank=True)
    total_paid_to_supplier = models.FloatField(null=True, blank=True)
    pending_amount_to_the_supplier = models.FloatField(null=True, blank=True)
    


class SupplierBatch(models.Model): #added when a record 
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    batch_date = models.DateField(auto_now_add=True)
    material_type = models.CharField(max_length=255, null=True, blank=True)
    price_per_ton = models.FloatField(null=True, blank=True)
    shipping = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Supplier Batch: {self.product_type} - {self.batch_date}"
    
@receiver(post_save, sender=RawMaterialRecord)
def create_supplier_batch(sender, instance, created, **kwargs):
    if created:
        supplier_batch = SupplierBatch.objects.create(
            supplier=instance.supplier,
            material_type=instance.material_type.name,
            price_per_ton=None,
            shipping=None,
            total=None
        )
        supplier_batch.save()
 
@receiver(pre_save, sender=SupplierBatch)
def calculate_total(sender, instance, **kwargs):
    if instance.shipping is not None and instance.price_per_ton is not None:
        instance.total = instance.shipping + instance.price_per_ton