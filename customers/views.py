from django.shortcuts import redirect, render, reverse
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import *
from .models import Customer
from .forms import CustomerForm , CustomerModelForm, CustomUserCreationForm


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse ("login")

class LandingPageView(TemplateView):
    template_name = "landing_page.html"

def landing_page(request):
    return render(request, "landing_page.html")

class CustomerListView(ListView):
    template_name = "customers/customer_list.html"
    queryset = Customer.objects.all()
    context_object_name = "customer"

def customer_list(request):
    customer = Customer.objects.all()
    context = {
        "customer" : customer
    }
    return render(request, "customers/customer_list.html" , context)

class CustomerDetailView(DetailView):
    template_name = "customers/customer_details.html"
    queryset = Customer.objects.all()
    context_object_name = "customer"


def customer_detail(request, pk):
    customer = Customer.objects.get(id=pk)
    context ={
        "customer" : customer
    }
    return render(request, "customers/customer_details.html" , context)

class CustomerCreteView(CreateView):
    template_name = "customers/customer_create.html"
    form_class = CustomerModelForm

    def get_success_url(self):
        return reverse ("customers:customer-list")


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

class CustomerUpdateView(UpdateView):
    template_name = "customers/customer_update.html"
    queryset = Customer.objects.all()
    form_class = CustomerModelForm

    def get_success_url(self):
        return reverse ("customers:customer-list")

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


class CustomerDeleteView(DeleteView):
    template_name = "customers/customer_delete.html"
    queryset = Customer.objects.all()

    def get_success_url(self):
        return reverse ("customers:customer-list")

def customer_delete(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return redirect("/customers")

