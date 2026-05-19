from django.db import models


class Tshirt(models.Model):

    SIZE_CHOICES = [
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
        ('XL','Extra Large'),
        ('XXL','Double XL')
    ]

    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to='tshirts/')

    description = models.TextField()

    price = models.IntegerField()



class Order(models.Model):

    tshirt_name = models.CharField(max_length=100)

    price = models.IntegerField()

    quantity = models.IntegerField()

    total_amount = models.IntegerField()

    customer_name = models.CharField(max_length=100)

    email = models.EmailField()

    address = models.TextField()

    size = models.CharField(max_length=5, choices=Tshirt.SIZE_CHOICES)