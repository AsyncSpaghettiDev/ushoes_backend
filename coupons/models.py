from django.db import models

# Create your models here.


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    discount = models.FloatField()
    remaining = models.IntegerField()
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField()

    def __str__(self):
        return self.code
