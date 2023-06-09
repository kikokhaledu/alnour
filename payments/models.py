from django.db import models
from django.forms import ValidationError

from suppliers.models import Supplier
from users.models import User

class SupplierPayment(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date = models.DateField()
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE)
    paid_amount = models.FloatField()
    
    def __str__(self):
        return f"payment to: {self.supplier.name}"  
    
    def clean(self):
        if self.supplier.pending_amount_to_the_supplier < self.paid_amount:
            raise ValidationError(f"Payment amount cannot be greater than the supplier's pending amount which is: {self.supplier.pending_amount_to_the_supplier}.")
        
        
# class cashflow_types:
#     # type_name = 
# class CashFlow(models.Model):
#     type = models.ForeignKey(cashflow_types,on_delete=models.CASCADE)
#     date = models.DateField()# auto
#     paid_amount = models.FloatField()
#     # supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True) # if type is supplier
    
    
    
    
"""
- i want to make a cash flow function  it should be able to have types this could be a cash in or cash out if its cash in 
- i will have to pick the client who gave me the cash from a drop down of the clients table
- amount 
- choose from my available products from the products table  as a drop down 
- date auto add now 
- when i add a chash in for the client i will get the client from the existing clients table and deduct the amount in the instance of this payment 
  from the client's pending amount 
- 
"""