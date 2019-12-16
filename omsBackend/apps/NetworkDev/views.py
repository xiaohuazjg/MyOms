from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from apps.NetworkDev.filters import NetdevFilterBackend
from apps.NetworkDev.serializers import NetdevSerializer
from apps.NetworkDev.models import NetworkDev


class NetdevViewSet(viewsets.ModelViewSet):
    filter_backends = (NetdevFilterBackend, DjangoFilterBackend, SearchFilter)
    queryset = NetworkDev.objects.all()
    serializer_class = NetdevSerializer
    filter_fields = ['netdev_asset', 'netdev_name', 'netdev_room', 'netdev_cabinet', 'netdev_position',
                  'netdev_procurement_date', 'netdev_boarding_date', 'netdev_supplier', 'netdev_manufacturer',
                 'netdev_sn', 'netdev_state', 'netdev_director', 'netdev_using_unit',
                  'netdev_power', 'netdev_U_num', 'netdev_type', 'netdev_ip', 'netdev_remarks', 'netdev_qr']

    search_fields = ['netdev_asset', 'netdev_name', 'netdev_room', 'netdev_cabinet', 'netdev_position',
                  'netdev_procurement_date', 'netdev_boarding_date', 'netdev_supplier',
                  'netdev_manufacturer', 'netdev_sn', 'netdev_state', 'netdev_director', 'netdev_using_unit',
                  'netdev_power', 'netdev_U_num', 'netdev_type', 'netdev_ip', 'netdev_remarks', 'netdev_qr']
