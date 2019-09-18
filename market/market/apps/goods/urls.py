from django.urls import path, re_path, include
from .views import CrabViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CrabViewSet)

urlpatterns = [
    re_path(r'^crab/', include(router.urls))
]
