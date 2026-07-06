from django.contrib import admin
from django.urls import path
from Books.views import books_view
from Members.views import members_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', books_view, name='books'),
    path('books', books_view),
    path('members/', members_view, name='members'),
    path('members', members_view),
]
