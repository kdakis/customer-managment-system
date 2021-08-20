from django.urls import path
from customers.views import customer_create, customer_list, customer_detail, customer_update, customer_delete

app_name = "customers"

urlpatterns = [

        path('',customer_list, name='customer-list'),
        path('<int:pk>/',customer_detail, name='customer-detail'),
        path('<int:pk>/update',customer_update, name='customer-update'),
        path('<int:pk>/delete',customer_delete, name='customer-delete'),
        path('create/',customer_create, name='customer-create'),


]