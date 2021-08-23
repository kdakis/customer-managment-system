from django.db.models import *
from django.core.paginator import *
from django.http import request
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin 
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

class CustomerListView(LoginRequiredMixin, ListView):
    context_object_name = "customer"

    def get(self,request):
        queryset = Customer.objects.all()
        search = request.GET.get('word','')

        if search:
            queryset = queryset.filter(
                Q(ssn__icontains=search)|
                Q(name__icontains=search)|
                Q(surname__icontains=search)|
                Q(phone__icontains=search)|
                Q(city__icontains=search)|
                Q(district__icontains=search)
            )
        
        context = {
        'customer': queryset, 
        'word': search
        }
        return render(request, "customers/customer_list.html", context)


def customer_list(request):
    customer = Customer.objects.all()
    context = {
        "customer" : customer
    }
    return render(request, "customers/customer_list.html" , context)

class CustomerDetailView(LoginRequiredMixin, DetailView):
    template_name = "customers/customer_details.html"
    queryset = Customer.objects.all()
    context_object_name = "customer"


def customer_detail(request, pk):
    customer = Customer.objects.get(id=pk)
    context ={
        "customer" : customer
    }
    return render(request, "customers/customer_details.html" , context)

class CustomerCreteView(LoginRequiredMixin, CreateView):
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

class CustomerUpdateView(LoginRequiredMixin, UpdateView):
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


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "customers/customer_delete.html"
    queryset = Customer.objects.all()

    def get_success_url(self):
        return reverse ("customers:customer-list")

def customer_delete(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return redirect("/customers")

