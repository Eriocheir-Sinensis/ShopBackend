from django.db import models
from django.utils.translation import gettext_lazy as _
from ..customer.models import Customer
from ..goods.models import Crab


class Cart(models.Model):
    cid = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('购物车')
        verbose_name_plural = _('购物车')

    def __str__(self):
        return "{}({})的购物车".format(self.customer.name, self.customer.phone)


class CartLineItem(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, related_name='cart_line_items', on_delete=models.CASCADE)
    crab = models.ForeignKey(Crab, verbose_name=_('大闸蟹'), on_delete=models.CASCADE)
    amount = models.IntegerField(_('数量'), default=0)

    class Meta:
        verbose_name = _('购物车物品')
        verbose_name_plural = _('购物车物品')

