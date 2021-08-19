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
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data ['name']
            surname = form.cleaned_data ['surname']
            ssn = form.cleaned_data ['ssn']
            phone = form.cleaned_data ['phone']
            city = form.cleaned_data ['city']
            district = form.cleaned_data ['district']
            
            Customer.objects.create(
                name = name,
                surname = surname,
                ssn = ssn,
                phone = phone,
                city = city,
                district = district
            )


    context = {
        "form" : form
    }
    return render(request, "customers/customer_create.html" , context)
