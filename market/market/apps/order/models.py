from django.db import models
from django.utils.translation import gettext_lazy as _
from ..customer.models import Customer
from ..goods.models import Crab

ORDER_STATUS = (
    ("未付款", "未付款"),
    ("已付款", "已付款"),
    ("已发货", "已发货"),
    ("完成", "完成")
)


class Order(models.Model):
    oid = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, verbose_name=_('客户'), on_delete=models.CASCADE)
    status = models.CharField(_('状态'), choices=ORDER_STATUS, max_length=10, default="未付款")
    receiver_name = models.CharField(_('收件人姓名'), max_length=80)
    receiver_phone = models.CharField(_('收件人电话'), max_length=80)
    receiver_address = models.CharField(_('收件人地址'), max_length=80)

    class Meta:
        verbose_name = _('订单')
        verbose_name_plural = _('订单')

    def description(self):
        return "{}({})的订单共{}件".format(self.customer.name, self.customer.phone, self.order_line_items.count())


class OrderLineItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, related_name='order_line_items', on_delete=models.CASCADE)
    crab = models.ForeignKey(Crab, verbose_name=_('大闸蟹'), on_delete=models.CASCADE)
    amount = models.IntegerField(_('数量'), default=0)

    class Meta:
        verbose_name = _('订单物品')
        verbose_name_plural = _('订单物品')

