from django.db import models
from datetime import datetime
# Create your models here.


class Parts(models.Model):

    parts_code = models.CharField(max_length=34, unique=True, blank=False, null=False, verbose_name="配件编号",
                                  help_text="配件编号")
    parts_type = models.CharField(max_length=32, blank=True, null=True, verbose_name="配件类型", help_text="配件类型")
    parts_details = models.CharField(max_length=32,  blank=True, null=True, verbose_name="配件明细", help_text="配件明细")
    parts_specs = models.CharField(max_length=32,  blank=True, null=True, verbose_name="配件规格", help_text="配件规格")
    parts_supplier = models.CharField(max_length=32,  blank=True, null=True, verbose_name="配件供应商",
                                      help_text="配件供应商")
    parts_brand = models.CharField(max_length=32,  blank=True, null=True, verbose_name="配件品牌", help_text="配件品牌")
    parts_asset_no = models.CharField(max_length=32,  blank=True, null=True, verbose_name="所属资产编号",
                                      help_text="所属资产编号")
    parts_status = models.CharField(max_length=16, blank=True, verbose_name="配件状态", help_text="配件状态")
    parts_date = models.DateField(default=datetime.now().date(), verbose_name="采购日期", help_text="采购日期")
    parts_remarks = models.TextField(max_length=2048, verbose_name="备注", help_text="备注")

    def __str__(self):
        return self.parts_type

    class Meta:
        verbose_name = "配件管理"
        verbose_name_plural = "配件管理"
