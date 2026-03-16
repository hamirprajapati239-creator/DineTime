from django import forms 
from.models import Reservation, TableBooking  
from.models import  ContactMessage, Restaurant, fooditem, Order, OrderDetail, Payment, Delivery


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactMessage
        fields = '__all__'

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'


class FoodItemForm(forms.ModelForm):
    class Meta:
        model = fooditem
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = '__all__'


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'

class TableBookingForm(forms.ModelForm):

    class Meta:
        model = TableBooking
        fields = ['name','email','phone','date','time','guests','message']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'type': 'time'}),
        }