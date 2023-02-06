from django.db import models
from shoes.models import Shoe
from coupons.models import Coupon
from login.models import ShippingAddress, Member

# Create your models here.

# which can be a good name for the model class to specify if the order will be shipped or received at the store


class OrderType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'order_types'
        verbose_name = 'Order Type'
        verbose_name_plural = 'Order Types'

# order must have a user, shoe, coupon, quantity, subtotal, total, date_created, date_updated, etc


class Order(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    order_type = models.ForeignKey(OrderType, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(
        ShippingAddress,
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
