from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)

class Employee_address(models.Model):
    address = models.CharField(max_length=100)