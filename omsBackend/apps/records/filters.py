# -*- coding: utf-8 -*-
# author: huashaw

from django_filters import rest_framework as filters
from django_filters import DateFromToRangeFilter
from apps.records.models import Record


class RecordFilter(filters.FilterSet):
    create_time = DateFromToRangeFilter()

    class Meta:
        model = Record
        fields = ['name', 'create_time']
