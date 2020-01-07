# -*- coding: utf-8 -*-
# author: huashaw
from rest_framework import serializers
from apps.bizmodule.models import BizModule


# class BizModuleSerializer3(serializers.ModelSerializer):
#     class Meta:
#         model = BizModule
#         fields = "__all__"
#
#
# class BizModuleSerializer2(serializers.ModelSerializer):
#     parent_biz = BizModuleSerializer3(many=True, allow_null=True)
#
#     class Meta:
#         model = BizModule
#         fields = "__all__"
#

class BizModuleSerializer(serializers.ModelSerializer):
    # parent_biz = BizModuleSerializer2(many=True, allow_null=True)
    class Meta:
        model = BizModule
        fields = "__all__"
