from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConfigurationViewSet, MeasurementUnitViewSet, DailyReportViewSet, ProductionRecordViewSet, RawMaterialRecordViewSet, SoldProductRecordViewSet

router = DefaultRouter()
router.register(r'configurations', ConfigurationViewSet)
router.register(r'measurementunits', MeasurementUnitViewSet)
router.register(r'dailyreports', DailyReportViewSet)
router.register(r'productionrecords', ProductionRecordViewSet)
router.register(r'rawmaterialrecords', RawMaterialRecordViewSet)
router.register(r'soldproductrecords', SoldProductRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
