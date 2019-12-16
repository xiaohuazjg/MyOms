from django.shortcuts import render

# Create your views here.

from apps.CabinetType.models import CabinetType
from apps.CabinetType.serializers import CabinetSerializer
from rest_framework import viewsets
from apps.CabinetType.filters import CabinetFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class CabinetViewSet(viewsets.ModelViewSet):
    filter_backends = (CabinetFilterBackend, DjangoFilterBackend, SearchFilter)
    queryset = CabinetType.objects.all()
    serializer_class = CabinetSerializer
    filter_fields = ['cabinet_code', 'cabinet_name']
    search_fields = ['cabinet_code', 'cabinet_name']
