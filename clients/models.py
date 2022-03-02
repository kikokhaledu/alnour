from django.db import models


############################################### clients##############################
class clients_table (models.Model):
	name = models.CharField(max_length= 255)
	total_amount_in_tons = models.IntegerField(null = True , blank = True)
	HQ_address = models.TextField(null = True,blank = True)
	shipping_address = models.TextField(null = True,blank = True)
	add_date = models.DateField(auto_now_add=True,null = True , blank = True)
	class Meta:
		verbose_name_plural = 'clients'
	def __str__(self):
		return self.name
