from django.contrib import admin
from django.urls import path
from Products.views import products_view
from Orders.views import orders_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', products_view, name='products'),
    path('products', products_view),
    path('orders/', orders_view, name='orders'),
    path('orders', orders_view),
]
