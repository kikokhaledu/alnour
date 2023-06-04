from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConfigurationViewSet, MaterialTypeViewSet, MeasurementUnitViewSet, DailyReportViewSet, NotificationViewSet, ProductTypeViewSet, ProductionRecordViewSet, RawMaterialRecordViewSet, SoldProductRecordViewSet, SupplierBatchViewSet, SupplierPaymentViewSet, SupplierViewSet

router = DefaultRouter()
router.register(r'configurations', ConfigurationViewSet)
router.register(r'measurementunits', MeasurementUnitViewSet)
router.register(r'dailyreports', DailyReportViewSet)
router.register(r'productionrecords', ProductionRecordViewSet)
router.register(r'rawmaterialrecords', RawMaterialRecordViewSet)
router.register(r'soldproductrecords', SoldProductRecordViewSet)
router.register(r'producttypes', ProductTypeViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'supplier_batches', SupplierBatchViewSet)
router.register(r'material_types', MaterialTypeViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'supplierpayments', SupplierPaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
