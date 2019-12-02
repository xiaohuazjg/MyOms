# -*- coding: utf-8 -*-
# author: kiven

from rest_framework import viewsets
from apps.wikis.models import Wiki
from apps.wikis.serializers import WikiSerializer
from apps.wikis.filters import WikiFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class WikiViewSet(viewsets.ModelViewSet):
    queryset = Wiki.objects.all().order_by('-update_time')
    serializer_class = WikiSerializer
    filter_backends = (WikiFilterBackend, DjangoFilterBackend, SearchFilter)
    search_fields = ['title', 'content']
    filter_fields = ['create_user__username', 'type__name']
