# -*- coding: utf-8 -*-
# author: huashaw

from rest_framework import serializers
from apps.records.models import Record


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['url', 'id', 'name', 'type', 'asset', 'method', 'before', 'after', 'diff', 'create_user', 'create_time']
