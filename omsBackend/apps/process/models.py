from django.db import models
from apps.servers.models import Servers, VMServers
# Create your models here.


class Process(models.Model):
    process_name = models.CharField(max_length=32, verbose_name="进程名", help_text="进程名")
    process_version = models.CharField(max_length=32, verbose_name="进程版本", help_text="进程版本")
    process_default_boot = models.CharField(max_length=132, verbose_name="默认启动路径", help_text="默认启动路径")
    process_type = models.CharField(max_length=32, verbose_name="进程类型", help_text="进程类型")
    process_quantity = models.IntegerField(verbose_name="进程数量",help_text="进程数量")
    process_enable_monitoring = models.BooleanField(blank=True,null=True, verbose_name="是否启用",
                                                    help_text="是否启用可以决定进程的监控")
    process_charge = models.CharField(max_length=32, verbose_name="负责人", help_text="负责人")
    process_port = models.IntegerField(verbose_name="端口号",help_text="具体程序占用的端口号")
    process_binding_IP = models.CharField(max_length=32, verbose_name="绑定IP ", help_text="0.0.0.0，或者具体的 IP")
    process_port_type = models.CharField(max_length=32, verbose_name="端口类型", help_text="对内还是对外")
    process_agreement = models.CharField(max_length=32, verbose_name="协议", help_text="协议")
    process_affiliated_process = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                                                   verbose_name="所属进程", help_text="属于什么进程")
    process_is_enabled = models.BooleanField(verbose_name="是否启用", help_text="启用、禁用")
    process_server = models.ForeignKey(Servers, null=True, blank=True, on_delete=models.SET_NULL,
                                       related_name="proc_server", verbose_name="所在服务器", help_text="所在服务器")
    process_vmserver = models.ForeignKey(VMServers, null=True, blank=True, on_delete=models.SET_NULL,
                                         related_name="proc_vm", verbose_name="所在虚拟机", help_text="所在虚拟机")

    def __str__(self):
        return self.process_name

    class Meta:
        verbose_name = "进程"
        verbose_name_plural = "进程"


class IPPortBinding(models.Model):

    ip_ip = models.CharField(max_length=32,  verbose_name="IP", help_text="IP")
    ip_port = models.CharField(max_length=8, verbose_name="端口号", help_text="端口号")
    ip_process = models.ForeignKey(Process, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="所属进程",
                                   related_name="ip_proc", help_text="所属进程")
    ip_server = models.ForeignKey(Servers, on_delete=models.SET_NULL,  blank=True, null=True,
                                  related_name="ip_servers", verbose_name="所属服务器", help_text="所属服务器")
    ip_vmserver = models.ForeignKey(VMServers, on_delete=models.SET_NULL,  blank=True, null=True,
                                    related_name="ip_vm", verbose_name="所属虚拟服务器", help_text="所属虚拟服务器")

    class Meta:
        unique_together = (('ip_ip', 'ip_port'),)
        verbose_name = "端口绑定"
        verbose_name_plural = verbose_name



