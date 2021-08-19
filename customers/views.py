from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm

def customer_list(request):

    customer = Customer.objects.all()

    context = {
        "customer" : customer
    }
    return render(request, "customers/customer_list.html" , context)

def customer_detail(request, pk):
    
    customer = Customer.objects.get(id=pk)
    context ={
        "customer" : customer
    }
    return render(request, "customers/customer_details.html" , context)

def customer_create(request):

    context = {
        "form" : CustomerForm()
    }
    return render(request, "customers/customer_create.html" , context)
