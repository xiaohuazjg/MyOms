# -*- coding: utf-8 -*-
# author: huashaw

from django_filters import rest_framework as filters
from apps.perms.models import UserMenuPerms


class UserMenuPermsFilter(filters.FilterSet):
    class Meta:
        model = UserMenuPerms
        fields = {
            'id': ['exact'],
            'group': ['exact'],
            'secondmenus__title': ['exact', 'contains'],
        }
