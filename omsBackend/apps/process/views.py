from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from apps.process.filters import ProcessFilterBackend, IPPortBindingFilterBackend
from apps.process.serializers import ProcessSerlizer, IPPortSerializer
from apps.process.models import Process, IPPortBinding
# Create your views here.


class ProcessViewSet(viewsets.ModelViewSet):
    filter_backends = (SearchFilter,DjangoFilterBackend,ProcessFilterBackend)
    serializer_class = ProcessSerlizer
    queryset = Process.objects.all()
    filter_fields = ['process_name', 'process_version', 'process_default_boot', 'process_type', 'process_quantity',
                  'process_enable_monitoring', 'process_charge', 'process_port', 'process_binding_IP',
                  'process_port_type', 'process_agreement', 'process_affiliated_process', 'process_is_enabled',
                  'process_server', 'process_vmserver']
    search_fields =  ['process_name', 'process_version', 'process_default_boot', 'process_type', 'process_quantity',
                  'process_enable_monitoring', 'process_charge', 'process_port', 'process_binding_IP',
                  'process_port_type', 'process_agreement', 'process_affiliated_process', 'process_is_enabled',
                  'process_server', 'process_vmserver']


class IPPortBindingViewSets(viewsets.ModelViewSet):
    filter_backends = (SearchFilter,DjangoFilterBackend,IPPortBindingFilterBackend)
    queryset = IPPortBinding.objects.all()
    serializer_class = IPPortSerializer
    filter_fields = ['ip_ip', 'ip_port', 'ip_process', 'ip_server', 'ip_vmserver']
    search_fields = ['ip_ip', 'ip_port', 'ip_process', 'ip_server', 'ip_vmserver']
