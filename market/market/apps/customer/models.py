from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Customer(AbstractUser):
    cid = models.AutoField(_('用户ID'), primary_key=True)
    name = models.CharField(_('姓名'), max_length=80)
    phone = models.CharField(_('电话号码'), max_length=80)
    address = models.CharField(_('地址'), max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = _('客户')
        verbose_name_plural = _('客户')

    def __str__(self):
        return self.name
