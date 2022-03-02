from django.db import models
from clients.models import clients_table
from django.contrib.postgres.functions import RandomUUID
import uuid

############################################### payment orders ##############################
class PO_table (models.Model):
	client = models.ForeignKey(clients_table,related_name='po',on_delete=models.CASCADE)
	po_number = models.UUIDField(primary_key=False, default=RandomUUID, editable=False,unique=True)
	invoice_number = models.UUIDField(primary_key=False, default=RandomUUID, editable=False,unique=True)
	issue_date = models.DateField(auto_now_add=True)
	invoice_date = models.DateField(auto_now_add=True)
	due_date = models.DateField(null = True , blank = True)
	invoice_period_start = models.DateField(null = True , blank = True)
	invoice_period_end = models.DateField(null = True , blank = True)
	#due date  date field  will alert me when there is a payment this week  in the upcoming payments tab
	class Meta:
		verbose_name_plural = 'POs'
	def __str__(self):
		return self.client.name +"'s"+' '+'PO'

############################################### invoices ##############################
class invoices_table (models.Model):
	item_name = models.CharField(max_length= 255)
	description = models.TextField(null = True,blank = True)
	unit_price = models.FloatField()
	quantity = models.IntegerField()
	sub_total = models.FloatField()
	item_total = models.FloatField()
	VAT = models.IntegerField(default = 14)# in percentage
	CIT = models.IntegerField(default = 1)# in percentage
	total = models.FloatField(null = True , blank = True)
	tax_reg_num = models.CharField(max_length= 255 , default = '618-665-959')
	CR_number = models.CharField(max_length= 255 , default = '160612')
	invoice_date = models.DateField(auto_now_add=True)
	bank_info = models.TextField(default = """National Bank OF EGYPT 
account number 6433171331027301011
account branch : Merag City Branch 
IBAN : EG 250003064331713310273010110""")
	invoice_footer = models.TextField(default = "info@alnourrrubber.com  |  +0201100671510  |  +0201000380435")
	address = models.TextField(default = """شركه النور للمنتجات المطاطيه
شارع علي حفظي متفرع من الشارع الجديد التبين حلوان""")
	PO = models.ForeignKey(PO_table,related_name='invoice',on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'invoices'
	def __str__(self):
		return self.item_name +' '+"invoice"


