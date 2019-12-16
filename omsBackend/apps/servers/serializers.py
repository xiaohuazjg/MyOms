# -*- coding: utf-8 -*-
# author: huashaw


from apps.servers.models import Servers, VMServers
from rest_framework import serializers


class ServersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servers
        fields = ['servers_asset_num', 'servers_room', 'servers_cabinet', 'servers_position', 'servers_host',
                  'servers_sn', 'servers_manufacturer', 'servers_model', 'servers_hostname', 'servers_business_dept',
                  'servers_team', "servers_business", 'servers_business_grade', 'servers_usage',
                  'servers_R_D_director', 'servers_oms_main', 'servers_backup_main', 'servers_procurement_date',
                  'server_shelf_time', 'servers_cofiguration_type', 'servers_raid', 'servers_status',
                  'servers_logical_region', 'servers_memory', 'servers_detailed', 'servers_remarks', 'servers_qr']


class VMServersSerializer(serializers.ModelSerializer):
    vm_asset_no = serializers.CharField(read_only=True)

    class Meta:
        model = VMServers
        fields = ['vm_host_name', 'vm_host_asset_no', 'vm_CPU_core', 'vm_detail_config', 'vm_remarks', 'vm_asset_no']

    def generate_vmserver_code(self, asset_no):
        # 获取记录总数
        vm_num = VMServers.objects.all().count()
        if vm_num is None:
            vm_num = 0

        vm_code = "{asset_no}VM{vm_code_str}".format(asset_no=asset_no, vm_code_str=str(vm_num).zfill(2))
        return vm_code

    def validate(self, attrs):
        attrs["vm_asset_no"] = self.generate_vmserver_code(attrs["vm_host_asset_no"])
        return attrs

