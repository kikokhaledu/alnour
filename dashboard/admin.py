from django.contrib import admin
from . models import orders,packed_rubber_shipments,notifications

admin.site.register(orders)
admin.site.register(packed_rubber_shipments)
admin.site.register(notifications)
