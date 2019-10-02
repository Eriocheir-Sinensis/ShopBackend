from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


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
    pic = models.ImageField(upload_to='api/img/crab_images/', verbose_name=_('图片'))

    class Meta:
        verbose_name = _('图片')
        verbose_name_plural = _('图片')

