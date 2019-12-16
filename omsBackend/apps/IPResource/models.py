from django.db import models

# Create your models here.
from apps.managelink.models import ManageLink
from apps.computer_room.models import ComputerRoom


class IPResource(models.Model):

    IP_State = (
        ("allocated", "已分配"),
        ("free", "空闲"),
        ("retain", "保留"),
    )

    IP_Type = (
        ("Public", "公网"),
        ("Intranet", "内网"),
        ("control", "控制"),
    )
    IP_Address = models.CharField(max_length=35, unique=True, blank=False, null=False, verbose_name="IP地址",
                                  help_text="IP地址")
    IP_Mask = models.CharField(max_length=35, blank=False, null=False, verbose_name="掩码地址", help_text="掩码地址")
    IP_Affiliated_link = models.ForeignKey(ManageLink, on_delete= models.SET_NULL, blank=True, null=True,
                                           related_name="ip_link", verbose_name="所属链路", help_text="所属链路")
    IP_Affiliated_Room = models.ForeignKey(ComputerRoom, on_delete= models.SET_NULL, blank=True, null=True,
                                           related_name="ip_room", verbose_name="所属机房", help_text="所属机房")
    IP_Status = models.CharField(max_length=32, choices=IP_State, verbose_name="IP地址状态", help_text="IP地址状态")

    IP_Equipment = models.CharField(max_length=32, null=True, blank=True, verbose_name="使用设备", help_text="使用设备")
    IP_User = models.CharField(max_length=32, null=True, blank=True, verbose_name="使用人", help_text="使用人")
    IP_Class = models.CharField(max_length=32, choices=IP_Type, verbose_name="IP地址类型", help_text="IP地址类型")

    IP_Remarks = models.TextField(max_length=1024, verbose_name="备注", help_text="备注")

    def __str__(self):
        return self.IP_Address

    class Meta:
        verbose_name = "IP资源"
        verbose_name_plural = "IP资源"

