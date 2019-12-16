from django.db import models
from apps.computer_room.models import ComputerRoom
# Create your models here.


class ManageLink(models.Model):

      """
      链路
      """
      Link_Status = {
        'using': '使用中',
        'offline': '下线'
        }

      Isp_Type = {
        "Telecom": "中国电信",
        "Unicom": "中国联通",
        "Mobile": "中国移动",
        "Education": "中国教育网",
        "Dedicated": "专线",
        "BGP": "BGP",
        "Other": "其他小运营商",
        "Abroad": "国外"
        }

      link_code = models.CharField(max_length=16, blank=False, verbose_name="链路编码", help_text="链路编码")
      link_name = models.CharField(max_length=32, blank=False, verbose_name="链路名称", help_text="链路名称")
      link_state = models.CharField(choices=Link_Status.items(), max_length=32, default="using",
                                  verbose_name="状态", help_text="状态")
      link_isp = models.CharField(choices=Isp_Type.items(), max_length=32, default="Telecom", verbose_name="ISP类型",
                                help_text="ISP类型")
      link_room = models.ForeignKey(ComputerRoom, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name = 'isp_room', verbose_name=u'机房')
      link_max_bandwidth = models.IntegerField(blank=True, null=True, verbose_name="采购最大带宽(兆)",
                                             help_text="采购最大带宽(百兆)")
      link_mix_bandwidth = models.IntegerField(blank=True, null=True, verbose_name="保底带宽(兆)",
                                             help_text="保底带宽(兆)")
      link_mix_cost = models.IntegerField(blank=True, null=True, verbose_name="保底费用(元/兆)",
                                             help_text="保底费用(元/兆)")
      link_unit_cost = models.IntegerField(blank=True, null=True, verbose_name="单位成本(元/兆)",
                                             help_text="单位成本(元/兆)")
      link_business = models.CharField(max_length=32, verbose_name="机房商务联系人", help_text="机房商务联系人")
      link_technical = models.CharField(max_length=32, verbose_name="机房技术联系人", help_text="机房技术联系人")
      link_phone = models.CharField(max_length=15, verbose_name="机房值班电话", help_text="机房值班电话")
      link_memo = models.CharField(max_length=256, verbose_name="备注", help_text="备注")

      def __str__(self):
        return self.link_name


      class Meta:
        verbose_name = "链路"
        verbose_name_plural = "链路"