from django.urls import path
from customers.views import customer_create, customer_list, customer_detail

app_name = "customers"

urlpatterns = [

        path('',customer_list),
        path('<int:pk>/',customer_detail),
        path('create/',customer_create),


]