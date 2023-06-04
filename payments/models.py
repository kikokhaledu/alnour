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