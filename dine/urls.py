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
     path('book-table/', views.book_table, name='book_table'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),





    # Restaurants
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurant/create/', views.restaurant_create, name='restaurant_create'),
    path('restaurant/update/<int:pk>/', views.restaurant_update, name='restaurant_update'),
    path('restaurant/delete/<int:pk>/', views.restaurant_delete, name='restaurant_delete'),

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
]




    

   
