from django.urls import path
from .views import CouponViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('', CouponViewSet, basename='coupons')

urlpatterns = router.urls
