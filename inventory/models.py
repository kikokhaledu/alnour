from django.db import models
from suppliers.models import suppliers_table
from products.models import products_table


#####################raw#########################

class raw_material (models.Model):
	name = models.CharField(max_length = 255)
	weight = models.FloatField()
	class Meta:
		verbose_name_plural = 'raw_material'
	def __str__(self):
		return self.name

# total raw material will be deducted from when we make a product 

##########################inventory of finished products:###############################
class finished_products (models.Model):
	product = models.ForeignKey(products_table,on_delete= models.CASCADE,related_name = 'finished_products')
	number_of_units = models.IntegerField()
	weight = models.FloatField()
	class Meta:
		verbose_name_plural = 'finished_products'
	def __str__(self):
		return self.product.name



############################################### batch##############################
class batch (models.Model):
	price_per_ton = models.FloatField()
	weight = models.FloatField()
	penalty = models.FloatField(default = 0)
	total_price = models.FloatField()
	supplier = models.ForeignKey(suppliers_table,on_delete= models.CASCADE,related_name = 'batch_suppliers')
	loader = models.BooleanField(default = True)
	data = models.DateField(auto_now_add = True)
	# shift
	comments = models.TextField()
	class Meta:
		verbose_name_plural = 'Batchs'
	def __str__(self):
		return 'Batch'+' '+str(self.date)
