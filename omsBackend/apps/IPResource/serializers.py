# -*- coding: utf-8 -*-
# author: huashaw

from rest_framework import serializers
from apps.IPResource.models import IPResource


class IPResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = IPResource
        fields = ["IP_Address", "IP_Mask", "IP_Affiliated_link", "IP_Affiliated_Room",
                  "IP_Status", "IP_Equipment", "IP_User", "IP_Class", "IP_Remarks"]