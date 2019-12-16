# -*- coding: utf-8 -*-
# author: huashaw


from apps.Parts.models import Parts
from rest_framework import serializers


class PartsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parts
        fields = ['parts_code', 'parts_type', 'parts_details', 'parts_specs', 'parts_supplier', 'parts_brand',
                  'parts_asset_no', 'parts_status', 'parts_date', 'parts_remarks']
