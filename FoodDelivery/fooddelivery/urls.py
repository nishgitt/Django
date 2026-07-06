from django.contrib import admin
from django.urls import path
from Restaurants.views import restaurants_view
from Menu.views import menu_view
from Orders.views import orders_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants/', restaurants_view, name='restaurants'),
    path('restaurants', restaurants_view),
    path('menu/', menu_view, name='menu'),
    path('menu', menu_view),
    path('orders/', orders_view, name='orders'),
    path('orders', orders_view),
]
