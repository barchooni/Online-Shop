from django.db import models
from User.models import Customer
from django.contrib.auth import get_user_model

User = get_user_model()

class History(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    cart = models.JSONField(default=dict)
    price = models.CharField(max_length=30)
    payment_method = models.CharField(max_length=30)
    tracking_code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.customer.username} --- {self.purchase_date}"

class Wallet(models.Model):
    
    holding = models.BigIntegerField()
    owner  = models.ForeignKey(User,on_delete=models.CASCADE)
