from django.contrib import admin
from .models import Reservation,Restaurant,fooditem,Order,OrderDetail,Payment,Delivery,TableBooking,ContactMessage



admin.site.register(TableBooking)
admin.site.register(ContactMessage)
admin.site.register(Reservation),
admin.site.register(Restaurant),
admin.site.register(fooditem),
admin.site.register(Order),
admin.site.register(OrderDetail),
admin.site.register(Payment),
admin.site.register(Delivery),

# Register your models here.
