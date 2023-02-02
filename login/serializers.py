from rest_framework.serializers import ModelSerializer
from .models import Role, ShippingAddress, Member


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class ShippingAddressSerializer(ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
