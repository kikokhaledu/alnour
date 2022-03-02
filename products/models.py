from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



####################################################product units#####################
class product_units(models.Model):
	unit_name = models.CharField(max_length= 255)
	class Meta:
		verbose_name_plural = 'units'
	def __str__(self):
		return self.unit_name

############################################### products##############################
class products_table (models.Model):
	name = models.CharField(max_length= 255)
	weight = models.FloatField()
	unit = models.ForeignKey(product_units,related_name='units',on_delete=models.CASCADE)
	class Meta:
		verbose_name_plural = 'products'
	def __str__(self):
		return self.name





# @receiver(post_save,sender = settings.AUTH_USER_MODEL)
# def create_toekn(sender,instance,created,**kwargs):
# 	if created:
# 		Token.objects.create(user=instance)