# -*- coding: utf-8 -*-
# author: huashaw


# Create your models here.
from django.db import models

Room_Status = {
    'testing': '测试中',
    'using': '使用中',
    'offline': '下线',
}


class ComputerRoom(models.Model):
    """
    机房

    """
    room_code = models.CharField(max_length=15, unique=True, verbose_name="机房编码", blank=False, help_text="机房编码")
    room_name = models.CharField(max_length=30, blank=False, verbose_name="机房名称", help_text="机房名称")
    room_status = models.CharField(choices=tuple(Room_Status.items()), max_length=32, default="testing",
                                   verbose_name="机房状态", help_text="机房状态")
    room_address = models.CharField(max_length=256, verbose_name="机房地址", help_text="机房地址")
    room_supplier = models.CharField(max_length=256, verbose_name="机房供应商", help_text="机房供应商")
    room_province = models.CharField(max_length=32, verbose_name="所在省份", help_text="所在省份")
    room_area = models.CharField(max_length=256, verbose_name="所在区域", help_text="所在区域")
    room_business = models.CharField(max_length=32, verbose_name="机房商务联系人", help_text="机房商务联系人")
    room_technical = models.CharField(max_length=32, verbose_name="机房技术联系人", help_text="机房技术联系人")
    room_receiving = models.CharField(max_length=32, verbose_name="机房收货联系人", help_text="机房收货联系人")
    room_phone = models.CharField(max_length=15, verbose_name="机房值班电话", help_text="机房值班电话")
    room_charge = models.CharField(max_length=32, verbose_name="机房运维负责人", help_text="机房运维负责人")
    room_memo = models.TextField(max_length=256, verbose_name="备注", help_text="备注")
    room_isEnable = models.BooleanField(blank=True, verbose_name="是否禁用", help_text="是否禁用", default=True)

    def __str__(self):
        return self.room_name

    class Meta:
        verbose_name = "机房"
        verbose_name_plural = "机房"
