from django.db import models
from clients.models import clients_table
from products.models import products_table
from workers.models import drivers



class orders(models.Model):
	client =models.ForeignKey(clients_table,related_name='order_client',on_delete=models.CASCADE,null = True ,blank = True)
	product = models.ForeignKey(products_table,related_name='order_product',on_delete=models.CASCADE,null = True ,blank = True)
	#order_number clientname and a number
	date_placed = models.DateField(auto_now_add = True)
	price_per_ton = models.FloatField()
	order_max_cap = models.IntegerField(default = 0)
	order_pending_ammount = models.FloatField(null=True,blank=True)
	completed = models.BooleanField(default = False)

	class Meta:
		verbose_name_plural = 'orders'
	def __str__(self):
		return self.client.name+"'s"+' '+'order'


class packed_rubber_shipments (models.Model):
	shipment_date = models.DateField()
	issuer_name = models.CharField(max_length= 255,default = 'AlNour Rubber')
	client = models.ForeignKey(clients_table,related_name='client',on_delete=models.CASCADE,null = True ,blank = True)
	additional_product = models.ForeignKey(products_table,related_name='additional_product',on_delete=models.CASCADE,null = True ,blank = True)
	oreder = models.ForeignKey(orders,related_name='order',on_delete=models.CASCADE)
	ammount = models.FloatField()#thresh hold to order max ammount
	driver = models.ForeignKey(drivers,related_name='drivers',on_delete=models.DO_NOTHING)#car plates number
	comments = models.TextField(null=True,blank=True)
	attestment = models.TextField(null=True,blank=True)
	additional_text = models.TextField(null=True,blank=True)


	class Meta:
		verbose_name_plural = 'packed rubber shipments'
	def __str__(self):
		return self.name
