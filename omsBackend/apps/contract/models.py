from django.db import models
from apps.Supplier.models import Supplier
# Create your models here.


class Contract(models.Model):
    Contract_Term = (
                     ('Long_term', u'长期'),
                     ('cycle', u'周期')
                     )

    contract_number = models.CharField(max_length=35, null=False, blank=False, verbose_name="合同编号",
                                       help_text="合同编号")
    contract_name = models.CharField(max_length=256, null=False, blank=False, verbose_name="合同名称",
                                     help_text="合同名称")
    contract_amount = models.DecimalField(decimal_places=10, max_digits=17, null=False, blank=False,
                                          verbose_name="合同金额(单位元)", help_text="合同金额(单位元)")
    contract_signing_date = models.DateField(null=False, blank=False, verbose_name="合同签署日期",
                                             help_text="合同签署日期")
    contract_start_date = models.DateField(null=False, blank=False, verbose_name="合同起始日期",
                                           help_text="合同起始日期")
    contract_end_date = models.DateField(null=False, blank=False, verbose_name="合同结束日期",
                                         help_text="合同结束日期")
    contract_term_type = models.CharField(choices=Contract_Term, max_length=34, verbose_name="合同期限类型",
                                          help_text="合同期限类型")
    contract_product_type = models.CharField(max_length=35, null=False, blank=False, verbose_name="关联产品类型",
                                             help_text="关联产品类型")
    contract_supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=False,
                                          related_name="cont_supp", verbose_name="供应商", help_text="供应商")
    contract_signed_by = models.CharField(max_length=35, null=False, blank=False, verbose_name="合同签订人",
                                          help_text="合同签订人")
    contract_remarks = models.TextField(max_length=2048, verbose_name="备注", help_text="备注")

    class Meta:
        verbose_name = "合同管理"
        verbose_name_plural = verbose_name


class ContractExpire(models.Model):
    contract_expire_number = models.CharField(max_length=35, null=False, blank=False,
                                              verbose_name="即将到期合同编号", help_text="即将到期合同编号")
    contract_expire_name = models.TextField(max_length=256, null=False, blank=False,
                                            verbose_name="即将到期合同名称", help_text="合同名称")
    contract_expire_end_date = models.DateField(null=False, blank=False, verbose_name="即将到期合同结束日期",
                                                help_text="即将到期合同结束日期")

    class Meta:
        verbose_name = "即将到期合同"
        verbose_name_plural = verbose_name
