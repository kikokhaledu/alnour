from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from suppliers.models import Supplier
from clients.models import Client
from products.models import ProductType, material_type
from payments.models import SupplierPayment
from notifications.models import Notification
from users.models import User

class Configuration(models.Model):
    """Model representing the global configuration of the system."""
    shifts_per_day = models.IntegerField(default=2)
    
class MeasurementUnit(models.Model):
    """Model representing a measurement unit."""
    name = models.CharField(max_length=255)
    weight = models.FloatField()
    
class DailyReport(models.Model):
    """Model representing a daily report."""
    SHIFT_CHOICES = [
        ('morning', 'Morning'),
        ('night', 'Night'),
    ]
    day = models.DateField()
    shift = models.CharField(max_length=7, choices=SHIFT_CHOICES)

class ProductionRecord(models.Model):
    """Model representing a production record."""
    daily_report = models.ForeignKey(DailyReport, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductType, on_delete=models.DO_NOTHING) # change to do nothing 
    measurement_unit = models.ForeignKey(MeasurementUnit, on_delete=models.DO_NOTHING) # change to do nothing 
    quantity = models.IntegerField(default=1)
    comment = models.TextField(blank=True)
    
class RawMaterialRecord(models.Model):
    """Model representing a raw material record."""
    daily_report = models.ForeignKey(DailyReport, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
    weight = models.FloatField()
    comment = models.TextField(blank=True)
    material_type = models.ForeignKey(material_type,on_delete=models.DO_NOTHING)
    notification_ids = models.TextField(blank=True)
    
class SoldProductRecord(models.Model):
    """Model representing a sold product record."""
    daily_report = models.ForeignKey(DailyReport, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductType, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    weight_sold = models.FloatField()
    address = models.CharField(max_length=255)
    comment = models.TextField(blank=True)

# Signals

@receiver(post_save, sender=RawMaterialRecord)
def create_notification(sender, instance, created, **kwargs):
    """Create a notification for each owner when a new raw material record is created."""
    if created:
        owners = User.objects.filter(userlevel__level='owner')
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

@receiver(pre_save, sender=RawMaterialRecord)
def delete_notifications(sender, instance, **kwargs):
    """Delete the notifications that were created when a raw material record is updated."""
    if instance.pk is not None and instance.notification_ids:
        notification_ids = map(int, instance.notification_ids.split(','))
        Notification.objects.filter(id__in=notification_ids).delete()
        instance.notification_ids = None
        instance.save(update_fields=['notification_ids'])

@receiver(post_save, sender=Supplier)
def calculate_total(sender, instance, **kwargs):
    """Calculate the total when the price per ton or shipping price of a supplier is updated."""
    if instance.price_per_ton is not None and instance.shipping_price is not None:
        instance.total = instance.price_per_ton + instance.shipping_price
        instance.save()

@receiver(post_save, sender=SupplierPayment) #  needs to be updated 
def update_supplier_totals(sender, instance, created, **kwargs):
    """Update the supplier's totals when a new payment is made to a supplier."""
    if created:
        supplier = instance.supplier
        supplier.total_amount_of_payments += instance.total_amount
        supplier.total_amount_pending = supplier.total - supplier.total_amount_of_payments
        supplier.save()
