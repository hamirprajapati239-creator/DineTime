from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Reservation(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.CharField(max_length=20)
    date=models.DateField()
    time=models.TimeField()
    numnber_of_people=models.PositiveIntegerField()
    restaurantImage = models.ImageField(upload_to='restaurant_images/',null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"



class Restaurant(models.Model):
    restaurant_name=models.CharField(max_length=100)
    location=models.CharField(max_length=150)
    contact_no=models.CharField(max_length=15)
    rating=models.FloatField(default=0.0)
    is_active=models.BooleanField(default=True)
    image=models.ImageField(upload_to="restaurants")
    class Meta:
        db_table = "Restaurant"

    def __str__(self):
         return self.restaurant_name
    
class fooditem(models.Model):
    Category_choices=(('veg','veg'),('non-veg','non-veg'),)
    
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    food_name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    category=models.CharField(max_length=10,choices=Category_choices)
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
    food_item = models.ForeignKey(fooditem, on_delete=models.CASCADE)
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


class TableBooking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    status = models.CharField(max_length=50, default="Confirmed")
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "TableBooking"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "ContactMessage"