from rest_framework.serializers import ModelSerializer
from .models import Shoe, ShoeColor, ShoeType, ShoeGender, Brand


class ShoeColorSerializer(ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = '__all__'


class ShoeTypeSerializer(ModelSerializer):
    class Meta:
        model = ShoeType
        fields = '__all__'


class ShoeGenderSerializer(ModelSerializer):
    class Meta:
        model = ShoeGender
        fields = '__all__'


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ShoeSerializer(ModelSerializer):
    class Meta:
        model = Shoe
        fields = '__all__'
