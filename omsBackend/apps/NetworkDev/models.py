from django.db import models

# Create your models here.
from apps.computer_room.models import ComputerRoom
from apps.CabinetType.models import CabinetType
from datetime import datetime


class NetworkDev(models.Model):
    # Netdev_State = {
    #     'netdev1': '交换机',
    #     'netdev2': '路由器',
    #     'netdev3': '防火墙',
    #     'netdev4': 'F5'
    # }

    # Netdev_Types = {
    #     'netdev5': '使用中',
    #     'netdev6': '库存',
    #     'netdev7': '搬迁中',
    #     'netdev8': '故障中',
    #     'netdev9': '下线中'
    # }

    netdev_asset = models.CharField(max_length=35, unique=True, verbose_name="资产编号", help_text="资产编号")
    netdev_name = models.CharField(max_length=128, verbose_name="设备名称", help_text="设备名称")
    netdev_room = models.ForeignKey(ComputerRoom, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name = 'netdev_room', verbose_name=u'所在机房')
    netdev_cabinet = models.ForeignKey(CabinetType, on_delete=models.SET_NULL, null=True, blank=True,
                                       related_name='netdev_cabinet', verbose_name=u'所在机架')
    netdev_position = models.IntegerField(blank=True, null=True, verbose_name="所在机架位", help_text="所在机架位")
    netdev_procurement_date = models.DateField(default=datetime.now().date(), verbose_name="采购时间", help_text="采购时间")
    netdev_boarding_date = models.DateField(default=datetime.now().date(), verbose_name="上架日期", help_text="上架日期")
    netdev_supplier = models.CharField(max_length=64, verbose_name="供应商", help_text="供应商", null=True, blank=True)
    netdev_manufacturer = models.CharField(max_length=64, verbose_name="制造商", help_text="制造商", null=True, blank=True)
    netdev_model = models.CharField(max_length=64, verbose_name="型号", help_text="型号", null=True, blank=True)
    netdev_sn = models.CharField(max_length=64, verbose_name="SN", help_text="SN", null=True, blank=True)
    netdev_state = models.CharField(max_length=32, verbose_name="状态", help_text="状态")
    netdev_director = models.CharField(max_length=64, verbose_name="运维负责人", help_text="运维负责人",
                                       null=True, blank=True)
    netdev_using_unit = models.CharField(max_length=64, verbose_name="使用业务部门", help_text="使用业务部门",
                                         null=True, blank=True)
    netdev_power = models.IntegerField(blank=True, null=True, verbose_name="额定功率", help_text="额定功率")
    netdev_U_num = models.IntegerField(blank=True, null=True, verbose_name="设备U数", help_text="设备占用机柜的U数")
    netdev_type = models.CharField(max_length=32, verbose_name="设备类型",
                                   help_text="设备类型")
    netdev_ip = models.CharField(max_length=64, verbose_name="管理 IP", help_text="管理 IP", null=True,
                                       blank=True)
    netdev_remarks = models.TextField(max_length=1024, verbose_name="备注", help_text="备注")
    netdev_qr = models.CharField(max_length=64, verbose_name="QR 码 ", help_text="QR 码 ", null=True,
                                       blank=True)

    def __str__(self):
        return self.netdev_name

    class Meta:
        verbose_name = "网络设备"
        verbose_name_plural = "网络设备"
