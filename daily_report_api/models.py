from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from suppliers.models import Supplier,SupplierBatch
from clients.models import Client
from products.models import ProductType, material_type
from payments.models import SupplierPayment
from notifications.models import Notification
from users.models import User
import logging

logger = logging.getLogger(__name__)

class Configuration(models.Model):
    """Model representing the global configuration of the system."""
    shifts_per_day = models.IntegerField(default=2)
    
    def __str__(self):
        return f"Configuration: {self.shifts_per_day} shifts per day"
    
class MeasurementUnit(models.Model):
    """Model representing a measurement unit."""
    name = models.CharField(max_length=255)
    weight = models.FloatField()
    
    def __str__(self):
        return self.name
     
class DailyReport(models.Model):
    """Model representing a daily report."""
    SHIFT_CHOICES = [
        ('morning', 'Morning'),
        ('night', 'Night'),
    ]
    day = models.DateField()
    shift = models.CharField(max_length=7, choices=SHIFT_CHOICES)
    
    def __str__(self):
        return f"Daily Report: {self.day} - {self.shift}"
    
    class Meta:
        unique_together = ('day', 'shift',)
        
class ProductionRecord(models.Model):
    """Model representing a production record."""
    daily_report = models.ForeignKey(DailyReport, on_delete=models.CASCADE, related_name='production_records')
    product_type = models.ForeignKey(ProductType, on_delete=models.DO_NOTHING) # change to do nothing 
    measurement_unit = models.ForeignKey(MeasurementUnit, on_delete=models.DO_NOTHING) # change to do nothing 
    quantity = models.IntegerField(default=1)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"Production Record: {self.product_type} - {self.quantity}"
   
class RawMaterialRecord(models.Model):
    """Model representing a raw material record."""
    daily_report = models.ForeignKey(DailyReport, on_delete=models.CASCADE, related_name='raw_material_records')
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
    weight = models.FloatField()
    comment = models.TextField(blank=True)
    material_type = models.ForeignKey(material_type,on_delete=models.DO_NOTHING)
    notification_ids = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return f"Raw Material Record: {self.supplier} - {self.weight}"  
    
class SoldProductRecord(models.Model):
    """Model representing a sold product record."""
    daily_report = models.ForeignKey(DailyReport, on_delete=models.CASCADE, related_name='sold_product_records')
    product_type = models.ForeignKey(ProductType, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    weight_sold = models.FloatField()
    address = models.CharField(max_length=255)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"Sold Product Record: {self.product_type} - {self.weight_sold}"
    
# Signals

@receiver(post_save, sender=RawMaterialRecord)
def create_notification(sender, instance, created, **kwargs):
    if created:
        try:
            owners = User.objects.filter(level='owner')
            notification_ids = []
            for owner in owners:
                notification = Notification.objects.create(
                    user=owner,
                    title="New Raw Material Record",
                    message=f"A new raw material record has been created for supplier {instance.supplier.name}. Please fill in the missing information."
                )
                notification_ids.append(str(notification.id))
            instance.notification_ids = ','.join(notification_ids)
            instance.save(update_fields=['notification_ids'])
        except Exception as e:
            logger.error(f"Error creating notification: {e}")

@receiver(pre_save, sender=RawMaterialRecord)
def delete_notifications(sender, instance, **kwargs):
    """Delete the notifications that were created when a raw material record is updated."""
    if instance.pk is not None and instance.notification_ids:
        notification_ids = map(int, instance.notification_ids.split(','))
        Notification.objects.filter(id__in=notification_ids).delete()
        instance.notification_ids = None
        instance.save(update_fields=['notification_ids'])


@receiver(post_save, sender=SupplierPayment) #  needs to be updated 
def update_supplier_totals(sender, instance, created, **kwargs):
    """Update the supplier's totals when a new payment is made to a supplier."""
    if created:
        supplier = instance.supplier
        supplier.total_paid_to_supplier += instance.paid_amount
        print(f"total paid to supplier{supplier.total_paid_to_supplier}")
        # when making a payment must make sure that there is enpough pending balance
        print(f"total pending: {supplier.pending_amount_to_the_supplier} - total paid to supplier {supplier.total_paid_to_supplier} ")
        supplier.pending_amount_to_the_supplier = supplier.pending_amount_to_the_supplier - instance.paid_amount
        print(f"total pending after {supplier.pending_amount_to_the_supplier}")
        supplier.save()


@receiver(post_save, sender=RawMaterialRecord)
def create_supplier_batch(sender, instance, created, **kwargs):
    if created:
        supplier_batch = SupplierBatch.objects.create(
            supplier=instance.supplier,
            material_type=instance.material_type.type_name,
            weight = instance.weight,
            price_per_ton=None,
            shipping=None,
            total=None
        )
        supplier_batch.save()


@receiver(pre_save, sender=SupplierBatch)
def calculate_total(sender, instance, **kwargs):
    if instance.shipping is not None and instance.price_per_ton is not None:
        instance.total = instance.shipping + instance.price_per_ton * instance.weight


@receiver(post_save, sender=SupplierBatch)
def calculate_supplier_total(sender, instance, **kwargs):
        supplier = instance.supplier
        batches = SupplierBatch.objects.filter(supplier=supplier)
        supplier.total_provided_from_supplier = sum(batch.total for batch in batches if batch.total is not None)
        supplier.shipping_total = sum(batch.shipping for batch in batches if batch.total is not None)
        supplier.pending_amount_to_the_supplier = supplier.total_provided_from_supplier - supplier.total_paid_to_supplier
        supplier.save()
