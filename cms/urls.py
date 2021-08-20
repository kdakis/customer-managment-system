from customers.views import LandingPageView
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name="landing-page"),
    path('customers/',include('customers.urls', namespace="customers")),
    path('login/', LoginView.as_view(), name="login")
]
