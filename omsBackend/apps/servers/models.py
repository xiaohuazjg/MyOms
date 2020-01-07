from django.db import models
from apps.computer_room.models import ComputerRoom
from apps.CabinetType.models import CabinetType
from datetime import datetime
import django

# Create your models here.


class Servers(models.Model):
    servers_asset_num = models.CharField(max_length=35, blank=False, null=False, verbose_name="资产编号",
                                         help_text="资产编号")
    servers_room = models.ForeignKey(ComputerRoom, related_name="server_room", on_delete=models.SET_NULL,
                                     null=True, blank=True, verbose_name=u'所在机房')
    servers_cabinet = models.ForeignKey(CabinetType, on_delete=models.SET_NULL, null=True, blank=True,
                                        related_name='server_cabinet', verbose_name=u'所在机架')
    servers_position = models.IntegerField(blank=True, null=True, verbose_name="所在机架位", help_text="所在机架位")
    servers_host = models.CharField(max_length=35, blank=False, null=False, verbose_name="所属宿主机",
                                    help_text="所属宿主机")
    servers_sn = models.CharField(max_length=35, blank=False, null=False, verbose_name="服务器SN",
                                  help_text="服务器SN")
    servers_manufacturer = models.CharField(max_length=35, blank=False, null=False, verbose_name="服务器制造商",
                                            help_text="服务器制造商")
    servers_model = models.CharField(max_length=35, blank=True, null=True, verbose_name="服务器型号",
                                     help_text="服务器型号")
    servers_hostname = models.CharField(max_length=36, blank=True, null=True, verbose_name="主机名",
                                        help_text="主机名")
    servers_business_dept = models.CharField(max_length=36, blank=True, null=True, verbose_name="所属业务部门",
                                             help_text="所属业务部门")
    servers_team = models.CharField(max_length=36, blank=True, null=True, verbose_name="所属运维小组",
                                    help_text="所属运维小组")
    servers_business = models.CharField(max_length=36, blank=True, null=True, verbose_name="所属业务",
                                        help_text="所属业务")
    servers_business_grade = models.CharField(max_length=36, blank=True, null=True, verbose_name="业务等级",
                                              help_text="业务等级")
    servers_usage = models.CharField(max_length=36, blank=True, null=True, verbose_name="使用用途",
                                     help_text="使用用途")
    servers_R_D_director = models.CharField(max_length=36, blank=True, null=True, verbose_name="研发负责人",
                                            help_text="研发负责人")
    servers_oms_main = models.CharField(max_length=36, blank=True, null=True, verbose_name="运维主负责人",
                                        help_text="运维主负责人")
    servers_backup_main = models.CharField(max_length=36, blank=True, null=True, verbose_name="运维备份负责人",
                                           help_text="运维备份负责人")
    servers_procurement_date = models.DateField(default=django.utils.timezone.now, verbose_name="采购时间",
                                                help_text="采购时间")
    server_shelf_time = models.DateField(default=django.utils.timezone.now, verbose_name="上架时间",
                                         help_text="上架时间")
    servers_cofiguration_type = models.CharField(max_length=32, verbose_name="配置类型", help_text="配置类型")
    servers_raid = models.CharField(max_length=32, verbose_name="RAID结构", help_text="RAID结构")
    servers_status = models.CharField(max_length=32, verbose_name="设备状态", help_text="设备状态")
    servers_logical_region = models.CharField(max_length=32, verbose_name="逻辑区域", help_text="逻辑区域")
    servers_memory = models.CharField(max_length=32, verbose_name="内存大小", help_text="内存大小")
    servers_detailed = models.TextField(max_length=1024, verbose_name="详细配置", help_text="详细配置")
    servers_remarks = models.TextField(max_length=2048, verbose_name="备注", help_text="备注")
    servers_qr = models.CharField(max_length=32, verbose_name="QR码", help_text="QR码")

    def __str__(self):
        return self.servers_hostname

    class Meta:
        verbose_name = "服务器"
        verbose_name_plural = "服务器"


class VMServers(models.Model):
    vm_host_name = models.CharField(max_length=32, verbose_name="虚拟机主机名称", help_text="虚拟机主机名称")
    vm_host_asset_no = models.ForeignKey(Servers, on_delete=models.SET_NULL, null=True, blank=True,
                                         related_name="vm_ser", verbose_name="所属宿主机资产编号",
                                         help_text="所属宿主机资产编号")
    vm_CPU_core = models.IntegerField(verbose_name="CPU核数", help_text="CPU核数")
    vm_detail_config = models.TextField(max_length=1024, verbose_name="详细配置", help_text="详细配置")
    vm_remarks = models.CharField(max_length=2048, verbose_name="备注", help_text="备注")
    vm_asset_no = models.CharField(max_length=32, verbose_name="虚拟机资产编号", help_text="虚拟机资产编号")

    def __str__(self):
        return self.vm_host_name

    class Meta:
        verbose_name = "虚拟机"
        verbose_name_plural = "虚拟机"
