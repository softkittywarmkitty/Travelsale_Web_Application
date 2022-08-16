from django.contrib import admin
from .models import Travelproduct, Type, Destination, Order, Payment, Paymethod, Staff, Customer

admin.site.register(Travelproduct)
admin.site.register(Type)
admin.site.register(Destination)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Paymethod)
admin.site.register(Staff)
admin.site.register(Customer)