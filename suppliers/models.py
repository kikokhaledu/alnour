from django.db import models
from products.models import products_table
from django.db.models.signals import post_save
from django.dispatch import receiver




############################################### suppliers ##############################
class suppliers_table (models.Model):
	name = models.CharField(max_length= 255)
	phone = models.CharField(max_length= 255,null = True,blank = True)
	cumulative_deliveries = models.FloatField(null = True,blank = True)
	price_per_ton = models.FloatField(null = True,blank = True)
	paied_ammounts = models.FloatField(null = True,blank = True)
	pending_ammounts = models.FloatField(null = True,blank = True)
	deducted_ammonunts = models.FloatField(null = True,blank = True)
	num_of_rejected_deliveries = models.IntegerField(null = True,blank = True)
	add_date = models.DateField(auto_now_add=True)
	product = models.ForeignKey(products_table,related_name='suplier_product',on_delete=models.CASCADE,null = True ,blank = True)
	# unit = models.ForeignKey(product_units,related_name='units',on_delete=models.CASCADE)
	# datetime filed  for each time they delvier a shipment
	class Meta:
		verbose_name_plural = 'Suppliers'
	def __str__(self):
		return self.name