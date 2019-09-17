from django.urls import path, re_path, include
from django.contrib import admin
from .views import LoginView, CustomerViewSet, CustomerCreateViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CustomerViewSet)

urlpatterns = [
    re_path(r'^login/?$', LoginView.as_view({'post': 'log'})),
    re_path(r'^register/?$', CustomerCreateViewSet.as_view({'post': 'create'})),
    re_path(r'', include(router.urls))
]
