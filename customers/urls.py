from django.urls import path
from customers.views import customer_create, customer_list, customer_detail, customer_update

app_name = "customers"

urlpatterns = [

        path('',customer_list),
        path('<int:pk>/',customer_detail),
        path('<int:pk>/update',customer_update),
        path('create/',customer_create),


]