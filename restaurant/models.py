from django.db import models
import datetime as dt


class Direction(models.Model):
    city = models.CharField(max_length=100)
    pc = models.CharField(max_length=20)
    street = models.CharField(max_length=60)
    int_number = models.IntegerField(blank=True, null=True)
    ext_number = models.IntegerField()
    state = models.TimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.city+' '+self.pc+' '+self.street+' '+' '+self.location


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    schedule_open = models.TimeField(auto_now=False, auto_now_add=False)
    schedule_close = models.TimeField(auto_now=False, auto_now_add=False)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    restaurant_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Create your models here.
