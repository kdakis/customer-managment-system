from django.db import models

class Customer(models.Model):

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    ssn = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)


