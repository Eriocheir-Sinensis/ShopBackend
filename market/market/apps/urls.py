from django.urls import path, re_path, include
from django.contrib import admin

urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'^customer/', include('market.apps.customer.urls')),
    re_path(r'^order/', include('market.apps.order.urls')),
    re_path(r'^cart/', include('market.apps.cart.urls')),
    re_path(r'^goods/', include('market.apps.goods.urls'))
]
