# -*- coding: utf-8 -*-
# author: huashaw

import time
from rest_framework import serializers
from apps.CabinetType.models import CabinetType


class CabinetSerializer(serializers.ModelSerializer):
    cabinet_code = serializers.CharField(read_only=True)

    class Meta:
        model = CabinetType
        fields = ['cabinet_code', 'cabinet_name', 'cabinet_have_UPS', 'cabinet_AB_power', 'cabinet_top_unused_U',
                  'cabinet_btm_unused_U', 'cabinet_pallets', 'cabinet_std_u', 'cabinet_flow', 'cabinet_power',
                  'cabinet_usable_U', 'cabinet_room', 'cabinet_floor', 'cabinet_state', 'cabinet_memo',
                  'cabinet_procurement_time']

    def generate_cabinet_code(self):
        # 获取记录总数
        cabinet_num = CabinetType.objects.all().count()
        if cabinet_num is None:
            cabinet_num = 0

        cabinet_code = "GT{time_str}{cabinet_code_str}".format(time_str=time.strftime("%Y%m%d"),

                                                         cabinet_code_str=str(cabinet_num).zfill(3))
        return cabinet_code

    def validate(self, attrs):
        attrs["cabinet_code"] = self.generate_cabinet_code()
        return attrs
