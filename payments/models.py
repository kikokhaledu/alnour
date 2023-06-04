from django.db import models

from suppliers.models import Supplier
from users.models import User

class SupplierPayment(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date = models.DateField()
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE)
    paid_amount = models.FloatField()