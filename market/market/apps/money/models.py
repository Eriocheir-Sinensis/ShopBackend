from django.db import models
from django.utils.translation import gettext_lazy as _


class Money(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(_('描述'), max_length=100)
    enabled = models.BooleanField(_('是否启用'), default=True)
    pic = models.ImageField(upload_to='api/img/money/', verbose_name=_('收款码图片'))

    class Meta:
        verbose_name = _('收款码')
        verbose_name_plural = _('收款码')

    def __str__(self):
        return self.description or self.pic.file.name
