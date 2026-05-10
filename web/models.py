from django.db import models

# Create your models here.
class customers(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    birthdate=models.DateField()
    moneyspent=models.IntegerField()
    anniversary=models.DateField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
class products(models.Model):
    category=models.CharField(max_length=20)
    price=models.IntegerField()

    def __str__(self):
       return self.category

class appuser(models.Model):
    username=models.CharField(max_length=50, unique=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    birthdate=models.DateField()
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=15)
    address=models.TextField()
    password=models.CharField(max_length=128)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"