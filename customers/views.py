from django.shortcuts import redirect, render
from django.http import HttpResponse 
from .models import Customer
from .forms import CustomerForm , CustomerModelForm

def landing_page(request):
    return render(request, "landing_page.html")

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
    form = CustomerModelForm()
    if request.method == "POST":
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/customers")
    context = {
        "form" : form
    }
    return render(request, "customers/customer_create.html" , context)

def customer_update(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerModelForm(instance=customer)
    if request.method == "POST":
        form = CustomerModelForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("/customers")
    context ={
        "form" : form,
        "customer" : customer
    }
    return render(request, "customers/customer_update.html" , context)

def customer_delete(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return redirect("/customers")

