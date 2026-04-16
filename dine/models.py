from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid



class TimeSlotCategory(models.Model):
    """Groups slots into 'Lunch', 'Dinner', etc."""
    NAME_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    ]
    name = models.CharField(max_length=20, choices=NAME_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Time Slot Categories"

    def __str__(self):
        return f"{self.name} ({self.start_time.strftime('%I:%M %p')} - {self.end_time.strftime('%I:%M %p')})"


class TimeSlot(models.Model):
    """The individual 15-min buttons (e.g., 12:15 PM)"""
    category = models.ForeignKey(TimeSlotCategory, related_name='slots', on_delete=models.CASCADE)
    specific_time = models.TimeField()
    discount_percentage = models.PositiveIntegerField(
        default=10, 
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ['specific_time']
        unique_together = ['category', 'specific_time']

    def __str__(self):
        return f"{self.category.name} @ {self.specific_time.strftime('%I:%M %p')} ({self.discount_percentage}% off)"
    

class Reservation(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
 
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(null=True)
    phone_number=models.CharField(max_length=20,null=True)
    date=models.DateField(null=True)
    number_of_people=models.PositiveIntegerField(null=True)
    restaurantImage = models.ImageField(upload_to='restaurant_images/',null=True, blank=True)
    selected_slot = models.ForeignKey(TimeSlot, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending',null=True) 
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    booking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE,null=True) # Link to your Restaurant model
    special_requests = models.TextField(blank=True, null=True)
    restaurantImage = models.ImageField(
        upload_to='restaurant_images/',
        null=True,
        blank=True
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True)
    address = models.TextField(null=True, blank=True)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    payment_status = models.BooleanField(default=False,null=True)
    def __str__(self):
        # FIX: Changed self.time_slot to self.selected_slot
        return f"{self.name} - {self.date} ({self.selected_slot})"
    def __str__(self):
        return f"{self.booking_id} | {self.name} - {self.date}"
        



class Booking(models.Model):
    # Ensure this matches exactly:
    razorpay_payment_id = models.CharField(max_length=100, null=True, blank=True)





class Restaurant(models.Model):
    restaurant_name=models.CharField(max_length=100)
    location=models.CharField(max_length=150)
    contact_no=models.CharField(max_length=15)
    rating=models.FloatField(default=0.0)
    is_active=models.BooleanField(default=True)
    restaurantImage=models.ImageField(upload_to="restaurant_images/",null=True,blank=True)
    cuisine = models.CharField(max_length=100, help_text="e.g. Continental, North Indian",null=True, blank=True)
    cost_for_two = models.IntegerField(default=0, help_text="Average cost for two people", null=True, blank=True)
    opening_time = models.TimeField(null=True, blank=True)
    closing_time = models.TimeField(null=True, blank=True)
    address = models.TextField( null=True, blank=True)
    class Meta:
        db_table = "Restaurant"

    def __str__(self):
         return self.restaurant_name
    
class RestaurantPhoto(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='photos',null=True,blank=True)
    image = models.ImageField(upload_to="restaurant_photos/",null=True, blank=True)
    caption = models.CharField(max_length=100, blank=True,null=True)

class Fooditem(models.Model):
    Category_choices=(('veg','veg'),('non-veg','non-veg'),)
    
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='fooditems',null=True,blank=True)
    food_name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    category=models.CharField(max_length=10,choices=Category_choices)
    image = models.ImageField(upload_to='food_images/', null=True, blank=True)
    availability=models.BooleanField(default=True)

    def __str__(self):
        return self.food_name
    class Meta:
        db_table="fooditems"

class Order(models.Model):
    STATUS_CHOICES= (('pending','pending'),('confirmed','confirmed'),('Delivered','Delivered'),('cancelled','cancelled'))
    Payment_status=(('paid',"paid"),('unpaid','unpaid'))

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending')
    payment_status = models.CharField(max_length=20, choices=Payment_status, default='Unpaid')

    def __str__(self):
         return f"Order #{self.id}"
    
    class Meta:
        db_table="Order"

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='order_details', on_delete=models.CASCADE)
    food_item = models.ForeignKey(Fooditem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.food_item.food_name} - {self.quantity}"
    
    class Meta:
        db_table="OrderDetail"

class Payment(models.Model):
    PAYMENT_METHODS=(('UPI','UPI'),('Card','Card'),('cash','cash'))
    PAYMENT_STATUS = (
        ("SUCCESS","SUCCESS"),("FAILED","FAILED"))
    order=models.OneToOneField(Order,on_delete=models.CASCADE)
    payment_method=models.CharField(max_length=50,choices=PAYMENT_METHODS)
    payment_date=models.DateTimeField(auto_now_add=True)
    payment_amount=models.DecimalField(max_digits=10,decimal_places=2)
    payment_status=models.CharField(max_length=20,choices=PAYMENT_STATUS)

    def __str__(self):
        return f"payment for order # {self.order.id}"
    class Meta:
        db_table="order"
    
    
class Delivery(models.Model):

    DELIVERY_STATUS=(
        ("assigned","assigned"),("on the way","on the way"), ("delivered","delivered"))
    order=models.OneToOneField(Order, on_delete=models.CASCADE)
    delivery_person = models.CharField(max_length=50)
    Delivery_status=models.CharField(max_length=30,choices=DELIVERY_STATUS)
    delivery_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Delivery for Order #{self.order.id}"
    
    class Meta:
        db_table="Delivery"
        verbose_name="Delivery"
        verbose_name_plural="Delivery"





class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "ContactMessage"


from django.db import models
from django.conf import settings

class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    profile_image = models.ImageField(
        upload_to="profile_images/",
        default="profile_images/default.png"
    )

    def __str__(self):
        return str(self.user)
    
from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('Starters', 'Starters'),
        ('Main Course', 'Main Course'),
        ('Beverages', 'Beverages'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    restaurantImage=models.ImageField(upload_to="restaurant_images/",null=True,blank=True)
    is_in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "MenuItem"


