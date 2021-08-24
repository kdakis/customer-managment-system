from django.urls import path
from customers.views import (
        CustomerCreteView,
        CustomerDeleteView,
        CustomerDetailView,
        CustomerListView,
        CustomerUpdateView
)

app_name = "customers"

urlpatterns = [

        path('', CustomerListView.as_view(), name='customer-list'),
        path('<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
        path('<int:pk>/update', CustomerUpdateView.as_view(), name='customer-update'),
        path('<int:pk>/delete', CustomerDeleteView.as_view(), name='customer-delete'),
        path('create/', CustomerCreteView.as_view(), name='customer-create'),

]
