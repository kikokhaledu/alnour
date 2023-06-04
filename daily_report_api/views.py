from rest_framework import viewsets
from notifications.models import Notification
from payments.models import SupplierPayment

from products.models import ProductType, material_type
from suppliers.models import Supplier, SupplierBatch
from .models import Configuration, MeasurementUnit, DailyReport, ProductionRecord, RawMaterialRecord, SoldProductRecord
from .serializers import ConfigurationSerializer, MaterialTypeSerializer, MeasurementUnitSerializer, DailyReportSerializer, NotificationSerializer, ProductTypeSerializer, ProductionRecordSerializer, RawMaterialRecordSerializer, SoldProductRecordSerializer, SupplierBatchSerializer, SupplierPaymentSerializer, SupplierSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class ConfigurationViewSet(viewsets.ModelViewSet):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer

class MeasurementUnitViewSet(viewsets.ModelViewSet):
    queryset = MeasurementUnit.objects.all()
    serializer_class = MeasurementUnitSerializer

class ProductionRecordViewSet(viewsets.ModelViewSet):
    queryset = ProductionRecord.objects.all()
    serializer_class = ProductionRecordSerializer

class RawMaterialRecordViewSet(viewsets.ModelViewSet):
    queryset = RawMaterialRecord.objects.all()
    serializer_class = RawMaterialRecordSerializer

class SoldProductRecordViewSet(viewsets.ModelViewSet):
    queryset = SoldProductRecord.objects.all()
    serializer_class = SoldProductRecordSerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierBatchViewSet(viewsets.ModelViewSet):
    queryset = SupplierBatch.objects.all()
    serializer_class = SupplierBatchSerializer

class MaterialTypeViewSet(viewsets.ModelViewSet):
    queryset = material_type.objects.all()
    serializer_class = MaterialTypeSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class SupplierPaymentViewSet(viewsets.ModelViewSet):
    queryset = SupplierPayment.objects.all()
    serializer_class = SupplierPaymentSerializer

class DailyReportViewSet(viewsets.ModelViewSet):
    queryset = DailyReport.objects.all()
    serializer_class = DailyReportSerializer
    