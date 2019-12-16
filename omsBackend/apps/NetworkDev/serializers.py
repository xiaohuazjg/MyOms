# -*- coding: utf-8 -*-
# author: huashaw

from apps.NetworkDev.models import NetworkDev
from rest_framework import serializers


class NetdevSerializer(serializers.ModelSerializer):

    class Meta:
        model = NetworkDev
        fields = ['netdev_asset', 'netdev_name', 'netdev_room', 'netdev_cabinet', 'netdev_position',
                   'netdev_procurement_date', 'netdev_boarding_date', 'netdev_supplier', 'netdev_manufacturer',
                  'netdev_sn', 'netdev_state', 'netdev_director', 'netdev_using_unit', 'netdev_power',
                  'netdev_U_num', 'netdev_type', 'netdev_ip', 'netdev_remarks', 'netdev_qr']
