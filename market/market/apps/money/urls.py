from django.urls import path, re_path, include
from .views import MoneyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', MoneyViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls))
]

