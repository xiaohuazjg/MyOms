# -*- coding: utf-8 -*-
# author: huashaw
import time
from rest_framework import serializers
from apps.computer_room.models import ComputerRoom


class ComputerRoomSerializer(serializers.ModelSerializer):
    room_code = serializers.CharField(read_only=True)

    class Meta:
        model = ComputerRoom
        fields = ['room_code', 'room_name', 'room_status', 'room_address', 'room_supplier', 'room_province',
                  'room_area', 'room_business', 'room_technical', 'room_receiving', 'room_phone', 'room_charge',
                  'room_memo', 'room_isEnable']


    def generate_room_code(self):
        # 获取记录总数
        room_num = ComputerRoom.objects.all().count()
        if room_num is None:
            room_num = 0

        room_code = "JF{time_str}{room_code_str}".format(time_str=time.strftime("%Y%m%d"),

                                                       room_code_str=str(room_num))
        return room_code

    def validate(self, attrs):
        attrs["room_code"] = self.generate_room_code()
        return attrs
