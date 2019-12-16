from django.db import models

# Create your models here.
from apps.computer_room.models import ComputerRoom
from datetime import datetime


class CabinetType(models.Model):

    Cabinet_Status = {
        'Notonline': '未上线',
        'inusing': '使用中',
        'offline': '下线'
    }

    cabinet_code = models.CharField(max_length=32, blank=True, null=True, verbose_name="机柜类型编码",
                                    help_text="机柜类型编码")
    cabinet_name = models.CharField(max_length=128, blank=True, null=True, help_text="机柜类型名称", verbose_name="机柜类型名称")
    cabinet_have_UPS = models.BooleanField(verbose_name="是否有UPS", help_text="是否有UPS")
    cabinet_AB_power = models.BooleanField(verbose_name="是否 A/B 路供电", help_text="是否 A/B 路供电")
    cabinet_top_unused_U = models.IntegerField(verbose_name="顶部不可用U数", help_text="顶部不可用U数")
    cabinet_btm_unused_U = models.IntegerField(verbose_name="底部不可用U数", help_text="底部不可用U数")
    cabinet_pallets = models.IntegerField(verbose_name="托盘数", help_text="托盘数")
    cabinet_std_u = models.IntegerField(verbose_name="机柜标准U数", help_text="机柜标准U数")
    cabinet_flow = models.IntegerField(verbose_name="机柜流量", help_text="机柜流量")
    cabinet_power = models.IntegerField(verbose_name="机柜功率(单路)", help_text="机柜功率(单路)")
    cabinet_usable_U = models.IntegerField(verbose_name="机柜可用U数", help_text="机柜可用U数")
    cabinet_room = models.ForeignKey(ComputerRoom, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='cabinet_room', verbose_name=u'所属机房')
    cabinet_floor = models.CharField(max_length=128, blank=True, null=True, help_text="所在楼层", verbose_name="所在楼层")
    cabinet_state = models.CharField(choices=Cabinet_Status.items(), max_length=32, default="inusing",
                                  verbose_name="机柜状态", help_text="机柜状态")
    cabinet_memo = models.CharField(null=True, max_length=256, verbose_name="备注", help_text="备注")
    cabinet_procurement_time = models.DateTimeField(default=datetime.now, verbose_name="采购时间", help_text="采购时间")

    def __str__(self):
        return self.cabinet_name

    class Meta:
        verbose_name = "机柜类型"
        verbose_name_plural = "机柜类型"