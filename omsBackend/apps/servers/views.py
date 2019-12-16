from django.shortcuts import render

# Create your views here.


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from apps.servers.filters import ServersFilterBackend, VMServersFilterBackend
from rest_framework import viewsets
from apps.servers.serializers import ServersSerializer, VMServersSerializer
from apps.servers.models import Servers, VMServers


class ServersViewSet(viewsets.ModelViewSet):
    serializer_class = ServersSerializer
    filter_backends = (ServersFilterBackend, SearchFilter, DjangoFilterBackend)
    queryset = Servers.objects.all()
    filter_fields = ['servers_asset_num', 'servers_room', 'servers_cabinet', 'servers_position', 'servers_host',
                  'servers_sn', 'servers_manufacturer', 'servers_model', 'servers_hostname', 'servers_business_dept',
                  'servers_team', "servers_business", 'servers_business_grade', 'servers_usage', 'servers_R_D_director',
                  'servers_oms_main', 'servers_backup_main', 'servers_procurement_date', 'server_shelf_time',
                  'servers_cofiguration_type', 'servers_raid', 'servers_status', 'servers_logical_region',
                  'servers_memory', 'servers_detailed', 'servers_remarks', 'servers_qr']

    search_fields = ['servers_asset_num', 'servers_room', 'servers_cabinet', 'servers_position', 'servers_host',
                  'servers_sn', 'servers_manufacturer', 'servers_model', 'servers_hostname', 'servers_business_dept',
                  'servers_team', "servers_business", 'servers_business_grade', 'servers_usage', 'servers_R_D_director',
                  'servers_oms_main', 'servers_backup_main', 'servers_procurement_date', 'server_shelf_time',
                  'servers_cofiguration_type', 'servers_raid', 'servers_status', 'servers_logical_region',
                  'servers_memory', 'servers_detailed', 'servers_remarks', 'servers_qr']


class VMServersViewSet(viewsets.ModelViewSet):
    serializer_class = VMServersSerializer
    filter_backends = (VMServersFilterBackend, SearchFilter, DjangoFilterBackend)
    queryset = VMServers.objects.all()
    filter_fields = ['vm_host_name', 'vm_host_asset_no', 'vm_CPU_core', 'vm_detail_config', 'vm_remarks']
    search_fields = ['vm_host_name', 'vm_host_asset_no', 'vm_CPU_core', 'vm_detail_config', 'vm_remarks']