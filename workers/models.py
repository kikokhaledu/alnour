from django.db import models
from shifts.models import shift_types_table
from django.contrib.postgres.fields import ArrayField


class drivers (models.Model):
	name = models.CharField(max_length= 255)
	licence = models.CharField(max_length= 255)
	number_of_shipments = models.IntegerField(default = 0)
	phone =  models.CharField(max_length= 255)
	class Meta:
		verbose_name_plural = 'drivers'
	def __str__(self):
		return self.name





class workers (models.Model):
	name = models.CharField(max_length= 255)
	id_number = models.CharField(max_length= 255)
	phone =  models.CharField(max_length= 255)
	hire_date = models.DateField(auto_now_add=True)
	number_of_shifts = models.IntegerField(null = True , blank = True)
	pay_ammount_per_shift = models.FloatField(default = 150.0)
	bonus = models.FloatField(null = True , blank = True)
	down_payments = models.FloatField(null = True , blank = True)
	deduction = models.FloatField(null = True , blank = True)
	last_payment_date = models.DateField(null = True , blank = True)
	upcoming_payment_date = models.DateField(null = True , blank = True)
	shifts = ArrayField(ArrayField(models.CharField(max_length= 255)))
	shift_type = models.ForeignKey(shift_types_table,related_name='shift_types',on_delete=models.CASCADE)
	class Meta:
		verbose_name_plural = 'workers'
	def __str__(self):
		return self.name
