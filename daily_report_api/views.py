from rest_framework import viewsets
from .models import Configuration, MeasurementUnit, DailyReport, ProductionRecord, RawMaterialRecord, SoldProductRecord
from .serializers import ConfigurationSerializer, MeasurementUnitSerializer, DailyReportSerializer, ProductionRecordSerializer, RawMaterialRecordSerializer, SoldProductRecordSerializer

class ConfigurationViewSet(viewsets.ModelViewSet):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer

class MeasurementUnitViewSet(viewsets.ModelViewSet):
    queryset = MeasurementUnit.objects.all()
    serializer_class = MeasurementUnitSerializer

class DailyReportViewSet(viewsets.ModelViewSet):
    queryset = DailyReport.objects.all()
    serializer_class = DailyReportSerializer

class ProductionRecordViewSet(viewsets.ModelViewSet):
    queryset = ProductionRecord.objects.all()
    serializer_class = ProductionRecordSerializer

class RawMaterialRecordViewSet(viewsets.ModelViewSet):
    queryset = RawMaterialRecord.objects.all()
    serializer_class = RawMaterialRecordSerializer

class SoldProductRecordViewSet(viewsets.ModelViewSet):
    queryset = SoldProductRecord.objects.all()
    serializer_class = SoldProductRecordSerializer
