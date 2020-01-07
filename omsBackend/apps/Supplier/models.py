from django.db import models

# Create your models here.


class Supplier(models.Model):
    supplier_no = models.CharField(max_length=35, verbose_name="供应商编号", help_text="供应商编号")
    supplier_name = models.CharField(max_length=35, verbose_name="供应商名称", help_text="供应商名称")
    supplier_addrss = models.CharField(max_length=256, verbose_name="供应商地址", help_text="供应商地址")
    business_contacts = models.CharField(max_length=35, verbose_name="商务联系人", help_text="商务联系人")
    business_contact_number = models.CharField(max_length=15, verbose_name="商务联系电话", help_text="商务联系电话")
    technical_contact = models.CharField(max_length=35, verbose_name="技术联系人", help_text="技术联系人")
    technical_contact_number = models.CharField(max_length=15, verbose_name="技术联系电话", help_text="技术联系电话")
    service_scope = models.TextField(max_length=2048, verbose_name="服务范围说明", help_text="服务范围说明")
    supplier_remarks = models.TextField(max_length=2048, verbose_name="备注", help_text="备注")

    class Mete:
        verbose_name = "供应商"
        verbose_name_plural = verbose_name
