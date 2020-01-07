from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class BizModule(MPTTModel):
    """
       业务层级
    """
    BIZ_LEVEL = (
        (1, "一级业务"),
        (2, "二级业务"),
        (3, "三级业务"),
    )

    biz_code = models.CharField(max_length=34, blank=False, null=False, verbose_name="业务编码",
                                help_text="业务编码")
    biz_name = models.CharField(max_length=128, blank=False, null=False, verbose_name="业务名称",
                                help_text="业务名称")
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                            related_name="parent_biz", verbose_name="上级业务名称", help_text="上级业务名称")
    biz_level = models.IntegerField(default=1, choices=BIZ_LEVEL, verbose_name="业务层级", help_text="业务层级")
    biz_desc = models.TextField(default="", verbose_name="业务描述", help_text="业务描述")

    class MPTTMeta:
        order_insertion_by = ['biz_name']
        verbose_name = "业务模块"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.biz_name

