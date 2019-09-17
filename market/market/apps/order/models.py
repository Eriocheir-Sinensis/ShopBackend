from django.db import models
from django.utils.translation import gettext_lazy as _
from ..customer.models import Customer

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

    class Meta:
        verbose_name = _('订单')
        verbose_name_plural = _('订单')

