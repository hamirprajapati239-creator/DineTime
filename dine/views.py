from urllib import request

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant,Reservation,TableBooking, ContactMessage,OrderDetail,Payment,Delivery,Order,TableBooking,fooditem
from .forms import FoodItemForm,RestaurantForm,OrderForm,OrderDetailForm,PaymentForm,DeliveryForm,ContactForm,TableBookingForm,ReservationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
def book_table(request):

    if request.method == "POST":
        form = TableBookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
        
            messages.success(request, "✅ Table booked successfully!")
            return redirect("my_bookings")   # FIXED

    else:
        form = TableBookingForm()

    return render(request, "book_table.html", {"form": form})


@login_required
def my_bookings(request):

    bookings = TableBooking.objects.filter(user=request.user)

    return render(request, "dine/user/my_bookings.html", {"bookings": bookings})

# CREATE

def restaurant_create(request):
    form = RestaurantForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('restaurant_list')
    return render(request, 'restaurant/create.html', {'form': form})


# READ
def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant/list.html', {'restaurants': restaurants})


# UPDATE
def restaurant_update(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    form = RestaurantForm(request.POST or None, instance=restaurant)
    if form.is_valid():
        form.save()
        return redirect('restaurant_list')
    return render(request, 'restaurant/update.html', {'form': form})


# DELETE
def restaurant_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    restaurant.delete()
    return redirect('restaurant_list')




def fooditem_list(request):
    items = fooditem.objects.all()
    return render(request, 'fooditem/list.html', {'items': items})


def fooditem_create(request):
    form = FoodItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fooditem_list')
    return render(request, 'fooditem/create.html', {'form': form})


def fooditem_update(request, pk):
    item = get_object_or_404(fooditem, pk=pk)
    form = FoodItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('fooditem_list')
    return render(request, 'fooditem/update.html', {'form': form})


def fooditem_delete(request, pk):
    item = get_object_or_404(fooditem, pk=pk)
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

    bookings = TableBooking.objects.filter(user=request.user)

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

    booking = get_object_or_404(TableBooking, id=id, user=request.user)

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




from django.shortcuts import render
from django.db.models import Q
from .models import Restaurant

def search_restaurant(request):

    query = request.GET.get('q')

    restaurants = Restaurant.objects.filter(
        Q(restaurant_name__icontains=query) |
        Q(location__icontains=query)
    )

    return render(request, "search_results.html", {
        "restaurants": restaurants,
        "query": query
    })
