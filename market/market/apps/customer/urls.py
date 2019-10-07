from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, LogoutView, CustomerViewSet, CustomerSelfViewSet, CustomerCreateViewSet

router = DefaultRouter()
router.register(r'', CustomerViewSet)

urlpatterns = [
    re_path(r'^login/?$', LoginView.as_view({'post': 'log'})),
    re_path(r'^logout/?$', LogoutView.as_view()),
    re_path(r'^register/?$', CustomerCreateViewSet.as_view({'post': 'create'})),
    re_path(r'^me/?$', CustomerSelfViewSet.as_view({'get': 'retrieve'})),
    re_path(r'', include(router.urls))
]
