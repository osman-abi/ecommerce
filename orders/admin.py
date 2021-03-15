from django.contrib import admin
from .models import (Order, ApprovedOrder, OrderItem)

admin.site.register(Order)
admin.site.register(ApprovedOrder)
admin.site.register(OrderItem)
# Register your models here.
