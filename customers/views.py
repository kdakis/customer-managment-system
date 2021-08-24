from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import *
from django.http import request
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import *
from .models import Customer
from .forms import CustomerModelForm, CustomUserCreationForm

DEFAULT_PAGINATE = 20


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse ("login")

class LandingPageView(TemplateView):
    template_name = "landing_page.html"


class CustomerListView(LoginRequiredMixin, ListView):
    context_object_name = "customer"
    
    def get(self,request):
        search = request.GET.get('s','')
        paginate_by = request.GET.get('p', DEFAULT_PAGINATE)
        queryset = Customer.objects.all()

        if search:
            queryset = queryset.filter(
                Q(ssn__icontains=search)|
                Q(name__icontains=search)|
                Q(surname__icontains=search)|
                Q(phone__icontains=search)|
                Q(city__icontains=search)|
                Q(district__icontains=search)
            )
        paginator = Paginator(queryset.order_by('-id'), paginate_by)
        page = request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
            
        context = {
        'customer': queryset, 
        's': search,
        'p': paginate_by
        }
        return render(request, "customers/customer_list.html", context)
        

class CustomerDetailView(LoginRequiredMixin, DetailView):
    template_name = "customers/customer_details.html"
    queryset = Customer.objects.all()
    context_object_name = "customer"


class CustomerCreteView(LoginRequiredMixin, CreateView):
    template_name = "customers/customer_create.html"
    form_class = CustomerModelForm

    def get_success_url(self):
        return reverse ("customers:customer-list")


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "customers/customer_update.html"
    queryset = Customer.objects.all()
    form_class = CustomerModelForm

    def get_success_url(self):
        return reverse ("customers:customer-list")


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "customers/customer_delete.html"
    queryset = Customer.objects.all()

    def get_success_url(self):
        return reverse ("customers:customer-list")