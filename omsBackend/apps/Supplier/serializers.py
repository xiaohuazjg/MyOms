# -*- coding: utf-8 -*-
# author: huashaw

from  rest_framework import serializers
from apps.Supplier.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = ['supplier_no', 'supplier_name', 'supplier_addrss','business_contacts', 'business_contact_number',
                  'technical_contact', 'technical_contact_number', 'service_scope', 'supplier_remarks']