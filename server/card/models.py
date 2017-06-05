"""card models"""
from django.db import models

from extension.modelutil import RandomFixedCharField


class Card(models.Model):
    """Card model."""
    uid = RandomFixedCharField('编号', max_length=16, unique=True)
    name = models.CharField('名称', max_length=32)

    short_intro = models.CharField('简介', max_length=512)

    creation_time = models.DateTimeField('创建时间', auto_now_add=True)
    updation_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        """Meta."""
        verbose_name = '卡片管理'
        verbose_name_plural = '卡片管理'
