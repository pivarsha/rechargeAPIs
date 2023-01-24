from django.db import models

# Create your models here.

class MobileRechargePlan(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    validity = models.IntegerField()
    network = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    plan = models.ForeignKey(MobileRechargePlan,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=100)
    network = models.CharField(max_length=50)

    def __str__(self):
        return self.network