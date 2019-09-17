from django.db import models
from django.utils.translation import gettext_lazy as _
from ..customer.models import Customer
from ..goods.models import Crab


class Cart(models.Model):
    cid = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    crabs = models.ForeignKey(Crab, related_name='crabs', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('购物车')
        verbose_name_plural = _('购物车')
