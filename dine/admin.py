from django.contrib import admin
from .models import Reservation,Restaurant,Fooditem,Order,OrderDetail,Payment,Delivery,ContactMessage, RestaurantPhoto
from .models import Reservation, TimeSlotCategory, TimeSlot

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    # We use 'get_slot_info' instead of just 'selected_slot'
    list_display = ('name', 'date', 'get_slot_info', 'status', 'created_at')
    list_filter = ('date', 'status', 'selected_slot__category')
    search_fields = ('name', 'email', 'phone_number')

    # This function formats the display in the list view
    @admin.display(ordering='selected_slot__specific_time', description='Time Slot')
    def get_slot_info(self, obj):
        if obj.selected_slot:
            # Displays as: Lunch - 12:15 PM (10% off)
            return f"{obj.selected_slot.category.name} - {obj.selected_slot.specific_time.strftime('%I:%M %p')} ({obj.selected_slot.discount_percentage}% off)"
        return "No slot selected"

@admin.register(TimeSlotCategory)
class TimeSlotCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'is_active')

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('specific_time', 'category', 'discount_percentage', 'is_available')
    list_filter = ('category', 'is_available')
admin.site.register(ContactMessage)
admin.site.register(Restaurant),
admin.site.register(Fooditem),
admin.site.register(Order),
admin.site.register(OrderDetail),
admin.site.register(Payment),
admin.site.register(Delivery),
admin.site.register(RestaurantPhoto)

# Register your models here.
