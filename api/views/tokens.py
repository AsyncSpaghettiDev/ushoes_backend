from rest_framework_simplejwt.views import TokenObtainPairView
from api.serializers.tokens import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
