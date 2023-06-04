from rest_framework import serializers

from notifications.models import Notification
from payments.models import SupplierPayment
from .models import Configuration, MeasurementUnit, DailyReport, ProductionRecord, RawMaterialRecord, SoldProductRecord
from products.models import ProductType, material_type
from suppliers.models import Supplier, SupplierBatch
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


class ProductionRecordSerializer(serializers.ModelSerializer):
    product_type = serializers.PrimaryKeyRelatedField(queryset=ProductType.objects.all())
    measurement_unit = serializers.PrimaryKeyRelatedField(queryset=MeasurementUnit.objects.all())

    class Meta:
        model = ProductionRecord
        fields = '__all__'
        
class RawMaterialRecordSerializer(serializers.ModelSerializer):
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    material_type = serializers.PrimaryKeyRelatedField(queryset=material_type.objects.all())

    class Meta:
        model = RawMaterialRecord
        fields = '__all__'

class SoldProductRecordSerializer(serializers.ModelSerializer):
    product_type = ProductTypeSerializer()
    client = ClientSerializer()

    class Meta:
        model = SoldProductRecord
        fields = '__all__'

class SupplierBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierBatch
        fields = '__all__'

class MaterialTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = material_type
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class SupplierPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierPayment
        fields = '__all__'
        
    def create(self, validated_data):
        supplier = validated_data.get('supplier')
        total_amount = validated_data.get('total_amount')

        if supplier.pending_amount_to_the_supplier < total_amount:
            raise serializers.ValidationError(
                f"Payment amount cannot be greater than the supplier's pending amount. "
                f"The current pending amount is {supplier.pending_amount_to_the_supplier}."
            )

        return super().create(validated_data)
          
class DailyReportSerializer(serializers.ModelSerializer):
    production_records = ProductionRecordSerializer(many=True, read_only=True)
    raw_material_records = RawMaterialRecordSerializer(many=True, read_only=True)
    sold_product_records = SoldProductRecordSerializer(many=True, read_only=True)

    class Meta:
        model = DailyReport
        fields = '__all__'