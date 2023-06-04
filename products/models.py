from django.db import models

class ProductType(models.Model):
    type_name = models.CharField(max_length=255)
    
    
class material_type(models.Model):
    type_name = models.CharField(max_length=255)