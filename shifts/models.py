from django.db import models

class shift_types_table (models.Model):
	name = models.CharField(max_length= 255)
	class Meta:
		verbose_name_plural = 'shift types'
	def __str__(self):
		return self.name


class shift_reports (models.Model):
	date = models.DateTimeField(auto_now_add = True)
	shift_type = models.ForeignKey(shift_types_table,related_name = 'shift_type',on_delete = models.DO_NOTHING)

	class Meta:
		verbose_name_plural = 'shift reports'
	def __str__(self):
		return str(self.date) + ' '+'Report' 