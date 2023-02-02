from django.urls import path
from .views import ShoeViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('', ShoeViewSet, basename='shoes')

urlpatterns = router.urls
