from shoes.serializers import ShoeSerializer
from coupons.serializers import CouponSerializer
from login.serializers import ShippingAddressSerializer, MemberSerializer

from rest_framework.serializers import ModelSerializer

from .models import OrderType, Order


class OrderTypeSerializer(ModelSerializer):
    class Meta:
        model = OrderType
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    user = MemberSerializer()
    shoe = ShoeSerializer()
    coupon = CouponSerializer()
    shipping_address = ShippingAddressSerializer()
    order_type = OrderTypeSerializer()

    class Meta:
        model = Order
        fields = '__all__'
