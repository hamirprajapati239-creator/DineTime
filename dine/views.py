from urllib import request

from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


from .decorators import role_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant,Reservation,ContactMessage,OrderDetail,Payment,Delivery,Order,Fooditem,MenuItem
from .forms import FoodItemForm,RestaurantForm,OrderForm,OrderDetailForm,PaymentForm,DeliveryForm,ContactForm,ReservationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TimeSlot,TimeSlotCategory
import uuid
from django.conf import settings
# Create your views here.
#@login_required(login_url="login") #check in core.urls.py login name should exist..
# def home(request):
#     return render(request, 'home.html')


#     from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def register(request):
    return render(request, 'register.html')
def login_user(request):
    return render(request, 'core/login.html')
def Menu(request):
    return render(request,'Menu.html')
def About(request):
    return render(request,'About.html')
def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


@role_required(allowed_roles=["owner"])
def ownerDashboardView(request):
    return render(request,"dine/owner/owner_dashboard.html")
#@login_required(login_url="login")
@role_required(allowed_roles=["user"])
def userDashboardView(request):
    return render(request,"dine/user/user_dashboard.html")
def reservation(request):
    if request.method == "POST":
        print(request.POST)
        form=ReservationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('owner_dashboard')
        else:
            form=ReservationForm()
    return render(request,"dine/owner/reservation.html",{'form':form})




@login_required
def my_bookings(request):
    bookings = Reservation.objects.filter(user=request.user).select_related('restaurant').order_by('-id')
    print(bookings.first().restaurant,".............................................")
    return render(request, 'dine/user/my_bookings.html', {'bookings': bookings})
def restaurant_create(request):
    form = RestaurantForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('restaurant_list')
    return render(request, 'restaurant/create.html', {'form': form})


# READ
# yourapp/views.py
from django.shortcuts import render
from .models import Restaurant  # Make sure this points to your models

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, "restaurants.html", {"restaurants": restaurants})
def restaurant_update(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    form = RestaurantForm(request.POST or None, instance=restaurant)
    if form.is_valid():
        form.save()
        return redirect('restaurant_list')
    return render(request, 'restaurant/update.html', {'form': form})
def restaurant_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    restaurant.delete()
    return redirect('restaurant_list')




def fooditem_list(request):
    items = Fooditem.objects.all()
    return render(request, 'fooditem/list.html', {'items': items})
def fooditem_create(request):
    form = FoodItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fooditem_list')
    return render(request, 'fooditem/create.html', {'form': form})
def fooditem_update(request, pk):
    item = get_object_or_404(Fooditem, pk=pk)
    form = FoodItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('fooditem_list')
    return render(request, 'fooditem/update.html', {'form': form})
def fooditem_delete(request, pk):
    item = get_object_or_404(Fooditem, pk=pk)
    item.delete()
    return redirect('fooditem_list')


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order/list.html', {'orders': orders})
def order_create(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('order_list')
    return render(request, 'order/create.html', {'form': form})
def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    form = OrderForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('order_list')
    return render(request, 'order/update.html', {'form': form})
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('order_list')
def orderdetail_list(request):
    details = OrderDetail.objects.all()
    return render(request, 'orderdetail/list.html', {'details': details})
def orderdetail_create(request):
    form = OrderDetailForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('orderdetail_list')
    return render(request, 'orderdetail/create.html', {'form': form})
def orderdetail_update(request, pk):
    detail = get_object_or_404(OrderDetail, pk=pk)
    form = OrderDetailForm(request.POST or None, instance=detail)
    if form.is_valid():
        form.save()
        return redirect('orderdetail_list')
    return render(request, 'orderdetail/update.html', {'form': form})
def orderdetail_delete(request, pk):
    detail = get_object_or_404(OrderDetail, pk=pk)
    detail.delete()
    return redirect('orderdetail_list')




def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment/list.html', {'payments': payments})
def payment_create(request):
    form = PaymentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('payment_list')
    return render(request, 'payment/create.html', {'form': form})
def payment_update(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    form = PaymentForm(request.POST or None, instance=payment)
    if form.is_valid():
        form.save()
        return redirect('payment_list')
    return render(request, 'payment/update.html', {'form': form})
def payment_delete(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    payment.delete()
    return redirect('payment_list')



def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request, 'delivery/list.html', {'deliveries': deliveries})
def delivery_create(request):
    form = DeliveryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('delivery_list')
    return render(request, 'delivery/create.html', {'form': form})
def delivery_update(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)
    form = DeliveryForm(request.POST or None, instance=delivery)
    if form.is_valid():
        form.save()
        return redirect('delivery_list')
    return render(request, 'delivery/update.html', {'form': form})
def delivery_delete(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)
    delivery.delete()
    return redirect('delivery_list')





@login_required
def dashboard(request):

    bookings = book_table.objects.filter(user=request.user)

    orders = Order.objects.filter(user=request.user)

    context = {

        "bookings": bookings.count(),
        "orders": orders.count()

    }

    return render(request, "dine/user/dashboard.html", context)


@login_required
def profile(request):

    return render(request, "dine/user/profile.html")



@login_required
def cancel_booking(request, id):

    booking = get_object_or_404(book_table, id=id, user=request.user)

    booking.delete()

    return redirect("my_bookings")


@login_required
def my_orders(request):

    orders = Order.objects.filter(user=request.user)

    return render(request, "dine/user/my_orders.html", {"orders": orders})


@login_required
def order_history(request):

    orders = Order.objects.filter(user=request.user)

    return render(request, "dine/user/order_history.html", {"orders": orders})



from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Restaurant, Fooditem


def search_restaurant(request):
    query = request.GET.get('q', '')

    if query:
        restaurants = Restaurant.objects.filter(
            Q(restaurant_name__icontains=query) |
            Q(location__icontains=query)
        )
    else:
        # ✅ THIS IS THE MAIN FIX
        restaurants = Restaurant.objects.all()

    return render(request, "search_results.html", {
        "restaurant": restaurants,
        "query": query
    })

# @login_required(login_url='login')
from django.shortcuts import render, get_object_or_404
from .models import Restaurant, Fooditem

def restaurant_detail(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    
    # Fetch all related data
    fooditems = restaurant.fooditems.all()
    photos = restaurant.photos.all() 

    # Directions Logic
    google_maps_url = ""
    if restaurant.address:
        google_maps_url = f"https://www.google.com/maps/search/?api=1&query={restaurant.address.replace(' ', '+')}"

    context = {
        "restaurant": restaurant,
        "fooditems": fooditems,
        "photos": photos,
        "google_maps_url": google_maps_url,
    }
    return render(request, "restaurant_detail.html", context)

from django.shortcuts import render
from .models import Profile

def user_profile(request):
    profile = Profile.objects.get(user=request.user)

    return render(request,'profile.html',{
        'profile':profile
    })




# owner
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def owner_dashboard(request):
    return render(request, 'dine/owner/owner_dashboard.html')

@login_required
def manage_menu(request):
    return render(request, 'dine/owner/manage_menu.html')

@login_required
def active_orders(request):
    return render(request, 'dine/owner/active_orders.html')

@login_required
def reservation(request):
    return render(request, 'dine/owner/reservation.html')

@login_required
def revenue(request):
    return render(request, 'dine/owner/revenue.html')

@login_required
def restaurant_settings(request):
    return render(request, 'dine/owner/restaurant_settings.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Reservation

# ==========================================
# USER FACING VIEWS (Booking Flow)
# ==========================================

  
from django.shortcuts import render, get_object_or_404
from .models import Restaurant


from django.shortcuts import render, get_object_or_404
from .models import Restaurant
from .forms import ReservationForm
import datetime
from django.shortcuts import render, get_object_or_404
from .models import Restaurant, TimeSlotCategory, Reservation
from .forms import ReservationForm

import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant, TimeSlotCategory, TimeSlot, Reservation
from .forms import ReservationForm
import razorpay
from datetime import date, timedelta

def book_table(request, restaurant_id):

    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    categories = TimeSlotCategory.objects.prefetch_related('slots').filter(is_active=True)

    today = date.today()
    date_list = []

    for i in range(7):
        day = today + timedelta(days=i)

        date_list.append({
            "full_date": day.strftime('%Y-%m-%d'),
            "day_name": "Today" if i == 0 else day.strftime('%a'),
            "display_date": day.strftime('%d %b')
        })

    # Handle form submission
    if request.method == "POST":

        form = ReservationForm(request.POST)

        selected_date = request.POST.get("date")
        selected_slot_id = request.POST.get("time")

        if form.is_valid():
            print(form.cleaned_data,"..............................................")
            
            #login user name email and  phone number will be automatically filled in form because of user model and reservation model relation and form is model form of reservation model.
            
            booking = form.save(commit=False)

            booking.restaurant = restaurant
              # Save to get an ID for the booking
            booking.date = selected_date
            if request.user.is_authenticated:
                booking.user = request.user
                # Fetching details from User object
                # Use 'first_name' or 'username' depending on your model
                print(request.user.email)
                booking.name = request.user.firstname or request.user.email.split('@')[0]  # Fallback to email prefix if firstName is not available
                booking.email = request.user.email
                booking.phone_number = "8460224296"

            # Save selected slot
            if selected_slot_id:
                booking.selected_slot = TimeSlot.objects.get(id=selected_slot_id)

            # Attach logged in user
            if request.user.is_authenticated:
                booking.user = request.user

            # Generate booking id
            booking.booking_id = uuid.uuid4()
             # 💰 Create Razorpay Order
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

            amount = 500 * 100  # ₹500 in paise (you can make dynamic)

            payment = client.order.create({
                "amount": amount,
                "currency": "INR",
                "payment_capture": "1"
            })

            booking.order_id = payment['id']
            booking.save()

            context = {
                "booking": booking,
                "razorpay_key": settings.RAZORPAY_KEY_ID,
                "amount": amount,
                "order_id": payment['id']
            }

            return render(request, "dine/user/payment.html", context)

    else:
        form = ReservationForm()

    return render(request, "dine/user/book_table.html", {
        "restaurant": restaurant,
        "categories": categories,
        "date_list": date_list,
        "form": form
    })

def payment_success(request):
    payment_id = request.GET.get("payment_id")
    order_id = request.GET.get("order_id")

    try:
        booking = Reservation.objects.get(order_id=order_id)

        booking.payment_id = payment_id
        booking.payment_status = True
        booking.status = "CONFIRMED"
        booking.save()

        return redirect('booking_success', booking_id=booking.booking_id)

    except Reservation.DoesNotExist:
        return HttpResponse("Invalid Payment", status=400)

def booking_success(request, booking_id):

    reservation = get_object_or_404(Reservation, booking_id=booking_id)

    return render(
        request,
        "dine/user/booking_success.html",
        {"booking": reservation}
    )
import razorpay
from datetime import datetime, timedelta
from django.http import JsonResponse








from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Reservation

import razorpay
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Booking





@receiver(post_save, sender=TimeSlotCategory)
def create_15_min_slots(sender, instance, created, **kwargs):
    """
    Automatically generates 15-minute intervals when a category is created.
    """
    if created:
        # Define the interval
        delta = datetime.timedelta(minutes=15)
        
        # We need a datetime object to do math (TimeField doesn't support timedeltas alone)
        dummy_date = datetime.date.today()
        current_dt = datetime.datetime.combine(dummy_date, instance.start_time)
        end_dt = datetime.datetime.combine(dummy_date, instance.end_time)

        slots_to_create = []

        while current_dt < end_dt:
            slots_to_create.append(
                TimeSlot(
                    category=instance,
                    specific_time=current_dt.time(),
                    discount_percentage=10 # Default discount
                )
            )
            current_dt += delta

        # Bulk create for better performance
        TimeSlot.objects.bulk_create(slots_to_create)

#


# ==========================================
# OWNER FACING VIEWS (Dashboard & Management)
# ==========================================

from django.shortcuts import render, redirect
from django.db.models import Sum, Count, Avg, Q
from django.contrib import messages
from .models import Reservation, Fooditem, Restaurant, Order
from datetime import date

def owner_dashboard(request):
    """
    Main Dashboard: High-level overview of performance.
    """
    today = date.today()
    
    # 1. Key Metrics
    # Filter by today's date if you want "Daily" stats, or leave as .count() for lifetime
    total_bookings = Reservation.objects.filter(date=today).count()
    
    # Sum up guests for today
    expected_guests = Reservation.objects.filter(date=today).aggregate(Sum('party_size'))['party_size__sum'] or 0
    
    # Calculate Total Revenue from Confirmed Reservations
    revenue_data = Reservation.objects.filter(status='Confirmed').aggregate(total=Sum('amount'))
    total_revenue = revenue_data['total'] or 0.00
    
    # 2. Table/Floor Status (Logic based on your HTML needs)
    # Assuming you have a field to track if a table is currently in use
    occupied_tables = Reservation.objects.filter(date=today, status='Confirmed').count() 
    available_tables = 20 - occupied_tables # Assuming 20 total tables

    # 3. Live Reservations Table (Recent 5)
    recent_reservations = Reservation.objects.select_related('selected_slot').order_by('-created_at')[:5]

    context = {
        'total_bookings': total_bookings,
        'expected_guests': expected_guests,
        'total_revenue': total_revenue,
        'recent_reservations': recent_reservations,
        'occupied_tables': occupied_tables,
        'available_tables': available_tables,
    }
    return render(request, 'dine/owner/owner_dashboard.html', context)

def reservation(request):
    bookings = Reservation.objects.select_related('selected_slot', 'restaurant').order_by('-date')
    return render(request, 'dine/owner/booking.html', {'bookings': bookings})

def revenue_page(request):
    # Summary Stats using Q for filtered counting
    stats = Reservation.objects.aggregate(
        total_amt=Sum('amount'),
        avg_per_booking=Avg('amount'),
        confirmed_count=Count('id', filter=Q(status='Confirmed')) 
    )
    
    transactions = Reservation.objects.filter(status='Confirmed').order_by('-date')
    
    context = {
        'total_revenue': stats['total_amt'] or 0,
        'avg_revenue': stats['avg_per_booking'] or 0,
        'confirmed_count': stats['confirmed_count'] or 0,
        'transactions': transactions,
    }
    return render(request, 'dine/owner/revenue.html', context)

def manage_menu(request):
    # Fetch all items
    all_items = Fooditem.objects.all()
    # Get unique categories to create sections
    categories = Fooditem.objects.values_list('category', flat=True).distinct()
    
    context = {
        'all_items': all_items,
        'categories': categories,
    }
    return render(request, 'dine/owner/manage_menu.html', context)

def restaurant_settings(request):
    restaurant = Restaurant.objects.first() 

    if request.method == "POST":
        restaurant.restaurant_name = request.POST.get('restaurant_name')
        restaurant.location = request.POST.get('location')
        restaurant.contact_no = request.POST.get('contact_no')
        
        image = request.FILES.get('restaurant_image')
        if image:
            restaurant.restaurantImage = image
        
        restaurant.save()
        messages.success(request, "Restaurant settings updated successfully!")
        return redirect('restaurant_settings')

    return render(request, 'dine/owner/restaurant_settings.html', {'restaurant': restaurant})

from django.contrib.auth import logout
from django.shortcuts import redirect, render

def logout_view(request):
    logout(request)
    return render(request, "logout.html")