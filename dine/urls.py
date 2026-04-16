from django.urls import path
from .import views


urlpatterns = [
    path("owner/",views.ownerDashboardView,name="owner_dashboard"),
    path("user/",views.userDashboardView,name="user_dashboard"),
    path('home/', views.home, name='home'),
    path('Menu/', views.Menu,name='Menu'),
    path('About/',views.About,name='About'),
    path('Contact/',views.contact,name='Contact'),
    path('reservation/',views.reservation,name='reservation'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),


 path(
        "book-table/<int:restaurant_id>/",
        views.book_table,
        name="book_table"
    ),

  
    path('booking-success/<uuid:booking_id>/', views.booking_success, name='booking_success'),
    path('manage-menu/', views.manage_menu, name='manage_menu'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('cancel-booking/<uuid:booking_id>/', views.cancel_booking, name='cancel_booking'),
    # path('confirm_booking/', views.confirm_booking, name='confirm_booking'),
   
    path('logout/', views.logout_view, name='logout'),


    path('payment-success/', views.payment_success, name='payment_success'),

    path('owner/', views.owner_dashboard, name='owner_dashboard'),
    path('owner/bookings/', views.reservation, name='reservation'),
    path('owner/menu/', views.manage_menu, name='manage_menu'),
    path('owner/revenue/', views.revenue_page, name='revenue'),
    path('owner/settings/', views.restaurant_settings, name='restaurant_settings'),

    # Restaurants
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurant/create/', views.restaurant_create, name='restaurant_create'),
    path('restaurant/update/<int:pk>/', views.restaurant_update, name='restaurant_update'),
    path('restaurant/delete/<int:pk>/', views.restaurant_delete, name='restaurant_delete'),
# yourapp/urls.py


    # path('restaurants/', views.restaurant_list, name='restaurant_list'),

    # FoodItem
    path('fooditems/', views.fooditem_list, name='fooditem_list'),
    path('fooditems/create/', views.fooditem_create, name='fooditem_create'),
    path('fooditems/update/<int:pk>/', views.fooditem_update, name='fooditem_update'),
    path('fooditems/delete/<int:pk>/', views.fooditem_delete, name='fooditem_delete'),

    # Order
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/update/<int:pk>/', views.order_update, name='order_update'),
    path('orders/delete/<int:pk>/', views.order_delete, name='order_delete'),

    # OrderDetail
    path('orderdetails/', views.orderdetail_list, name='orderdetail_list'),
    path('orderdetails/create/', views.orderdetail_create, name='orderdetail_create'),
    path('orderdetails/update/<int:pk>/', views.orderdetail_update, name='orderdetail_update'),
    path('orderdetails/delete/<int:pk>/', views.orderdetail_delete, name='orderdetail_delete'),    
    
    # Payment
    path('payments/', views.payment_list, name='payment_list'),     
    path('payments/create/', views.payment_create, name='payment_create'),
    path('payments/update/<int:pk>/', views.payment_update, name='payment_update'),
    path('payments/delete/<int:pk>/', views.payment_delete, name='payment_delete'),



    #deliveries
    path('deliveries/', views.delivery_list, name='delivery_list'),
    path('deliveries/create/', views.delivery_create, name='delivery_create'),
    path('contact/', views.contact, name="contact"),


    path('dashboard/', views.dashboard, name="dashboard"),
    path("profile/",views.profile,name="profile"),
    path("my-bookings/",views.my_bookings,name="my_bookings"),
    path('cancel-booking/<int:id>/', views.cancel_booking, name="cancel_booking"),
    path('my-orders/', views.my_orders, name="my_orders"),
    path('order-history/', views.order_history, name="order_history"),


    #search_resturant

    path('search/', views.search_restaurant, name='search_restaurant'),
    path('restaurant/<int:id>/', views.restaurant_detail, name='restaurant_detail'),
    path('profile/',views.user_profile,name='profile'),



    path('owner/', views.owner_dashboard, name='owner_dashboard'),
    path('owner/menu/', views.manage_menu, name='manage_menu'),
    path('owner/orders/', views.active_orders, name='active_orders'),
    path('owner/reservation/', views.reservation, name='reservations'),
    path('owner/revenue/', views.revenue, name='revenue'),
    path('owner/settings/', views.restaurant_settings, name='restaurant_settings'),
]






    

   
