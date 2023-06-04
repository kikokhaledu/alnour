from django.db import models

class ProductType(models.Model):
    type_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.type_name
    
    
class material_type(models.Model):
    type_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.type_name