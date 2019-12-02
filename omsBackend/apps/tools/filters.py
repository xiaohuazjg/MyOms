# -*- coding: utf-8 -*-
# author: huashaw

from django_filters import rest_framework as filters
from apps.tools.models import Calender


class CalenderFilter(filters.FilterSet):
    class Meta:
        model = Calender
        fields = {
            'title': ['exact', 'contains'],
            'start': ['gte'],
            'end': ['lte'],
        }