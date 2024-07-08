from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200, default='') 
    contact = models.CharField(max_length=200, default='')
    # active = models.IntegerField()

class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name="orders", on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    total_in_cents = models.IntegerField()

    def __str__(self):
        return self.description
    
    