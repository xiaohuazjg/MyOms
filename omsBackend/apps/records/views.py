# -*- coding: utf-8 -*-
# author: huashaw

from rest_framework import viewsets
from apps.records.models import Record
from apps.records.serializers import RecordSerializer
from apps.records.filters import RecordFilter


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all().order_by('-create_time')
    serializer_class = RecordSerializer
    filter_class = RecordFilter
    search_fields = ['asset']

