from django.contrib import admin
from django.urls import path
from Accounts.views import accounts_view
from Loans.views import loans_view
from Transactions.views import transactions_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', accounts_view, name='accounts'),
    path('accounts', accounts_view),
    path('loans/', loans_view, name='loans'),
    path('loans', loans_view),
    path('transactions/', transactions_view, name='transactions'),
    path('transactions', transactions_view),
]
