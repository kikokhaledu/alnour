from rest_framework import serializers
from .models import Configuration, MeasurementUnit, DailyReport, ProductionRecord, RawMaterialRecord, SoldProductRecord
from products.models import ProductType
from suppliers.models import Supplier
from clients.models import Client

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = '__all__'

class MeasurementUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementUnit
        fields = '__all__'

class DailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = '__all__'

class ProductionRecordSerializer(serializers.ModelSerializer):
    product_type = ProductTypeSerializer()
    measurement_unit = MeasurementUnitSerializer()

    class Meta:
        model = ProductionRecord
        fields = '__all__'
        
class RawMaterialRecordSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()

    class Meta:
        model = RawMaterialRecord
        fields = '__all__'

class SoldProductRecordSerializer(serializers.ModelSerializer):
    product_type = ProductTypeSerializer()
    client = ClientSerializer()

    class Meta:
        model = SoldProductRecord
        fields = '__all__'