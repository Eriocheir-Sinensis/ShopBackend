from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Customer(User):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(_('姓名'), max_length=80)
    phone = models.CharField(_('电话号码'), max_length=80)
    address = models.CharField(_('地址'), max_length=300)

    class Meta:
        verbose_name = _('客户')
        verbose_name_plural = _('客户')

    def __str__(self):
        return self.name


class Crab(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(_('名称'), max_length=80, unique=True)
    size = models.CharField(_('大小'), max_length=80)
    price = models.IntegerField(_('实际价格'), default=100)
    original_price = models.IntegerField(_('原价'), null=True, blank=True)
    net = models.CharField(_('单位'), default='元', max_length=80)
    description = models.TextField(_('描述'), max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = _('大闸蟹')
        verbose_name_plural = _('大闸蟹')

    def __str__(self):
        return self.name


class CrabImage(models.Model):
    iid = models.AutoField(primary_key=True)
    crab = models.ForeignKey(Crab, related_name='images', on_delete=models.DO_NOTHING)
    pic = models.ImageField(upload_to='img/crab_images/', verbose_name=_('图片'))

    class Meta:
        verbose_name = _('图片')
        verbose_name_plural = _('图片')


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


class Cart(models.Model):
    cid = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    crabs = models.ForeignKey(Crab, related_name='crabs', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('购物车')
        verbose_name_plural = _('购物车')


class LineItem(models.Model):
    lid = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    crab = models.ForeignKey(Crab, verbose_name=_('大闸蟹'), on_delete=models.CASCADE)
    amount = models.IntegerField(_('数量'), default=0)

    class Meta:
        verbose_name = _('物品')
        verbose_name_plural = _('物品')


