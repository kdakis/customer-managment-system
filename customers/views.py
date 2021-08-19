from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

def index(request):

    customer = Customer.objects.all()

    context = {
        "customer" : customer
    }

    return render(request, "second.html" , context)