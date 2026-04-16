from django import forms 
from.models import Reservation 
from.models import  ContactMessage, Restaurant, Fooditem, Order, OrderDetail, Payment, Delivery


# forms.py example
from django import forms

from django import forms
from .models import Reservation
from django import forms
from .models import Reservation, TimeSlot

class ReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # We catch a 'category_name' (e.g., 'Lunch') passed from the view
        category_name = kwargs.pop('category_name', None)
        super(ReservationForm, self).__init__(*args, **kwargs)
        
        # This filters the dropdown to only show relevant, available slots
        if category_name:
            self.fields['selected_slot'].queryset = TimeSlot.objects.filter(
                category__name=category_name,
                is_available=True
            ).order_by('specific_time')
        else:
            # Default to showing no slots until a category is known
            self.fields['selected_slot'].queryset = TimeSlot.objects.none()

    class Meta:
        model = Reservation
        fields = ['number_of_people', 'date', 'selected_slot']
        
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'name@example.com', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '+91 98765 43210', 'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'number_of_people': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'}),
            'selected_slot': forms.Select(attrs={'class': 'form-control'}),
        }
        
        labels = {
            'selected_slot': 'Available Time Slots',
            'number_of_people': 'Guests',
        }
            # Add 'form-control' class if you prefer handling it in Python instead of CSS

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
        model = Fooditem
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

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = Fooditem
        fields = '__all__'


