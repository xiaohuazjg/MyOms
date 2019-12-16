# -*- coding: utf-8 -*-
# author: huashaw

from rest_framework import  serializers
from apps.process.models import Process, IPPortBinding


class ProcessSerlizer(serializers.ModelSerializer):

    class Meta:
        model = Process
        fields = ['process_name', 'process_version', 'process_default_boot', 'process_type', 'process_quantity',
                  'process_enable_monitoring', 'process_charge', 'process_port', 'process_binding_IP',
                  'process_port_type', 'process_agreement', 'process_affiliated_process', 'process_is_enabled',
                  'process_server', 'process_vmserver']

class IPPortSerializer(serializers.ModelSerializer):

    class Meta:
        model = IPPortBinding
        fields = ['ip_ip', 'ip_port', 'ip_process', 'ip_server', 'ip_vmserver']
