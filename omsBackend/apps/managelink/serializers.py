# -*- coding: utf-8 -*-
# author: huashaw

import time
from rest_framework import serializers
from apps.managelink.models import ManageLink


class ManageLinkSerializer(serializers.ModelSerializer):
    link_code = serializers.CharField(read_only=True)

    class Meta:
        model = ManageLink
        fields = ['link_code', 'link_name', 'link_state', 'link_isp', 'link_room', 'link_max_bandwidth',
                  'link_mix_bandwidth', 'link_mix_cost', 'link_unit_cost',  'link_business', 'link_technical',
                  'link_phone', 'link_memo']


    def generate_link_code(self):
        # 获取记录总数
        link_num = ManageLink.objects.all().count()
        if link_num is None:
            link_num = 0

        room_code = "LN{time_str}{link_code_str}".format(time_str=time.strftime("%Y%m%d"),

                                                       link_code_str=str(link_num))
        return room_code

    def validate(self, attrs):
        attrs["link_code"] = self.generate_link_code()
        return attrs
