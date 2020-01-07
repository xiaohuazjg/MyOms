# -*- coding: utf-8 -*-
# author: huashaw

from rest_framework import serializers
from apps.contract.models import Contract, ContractExpire


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = ['contract_number', 'contract_name', 'contract_amount', 'contract_signing_date',
                  'contract_start_date', 'contract_end_date', 'contract_term_type', 'contract_product_type',
                  'contract_supplier', 'contract_signed_by', 'contract_remarks']


class ContractExpireSerializer(serializers.ModelSerializer):
    contract_expire_number = serializers.CharField(read_only=True)
    contract_expire_name = serializers.CharField(read_only=True)
    contract_expire_end_date = serializers.DateField(read_only=True)

    class Meta:
        model = ContractExpire
        fields =['contract_expire_number', 'contract_expire_name', 'contract_expire_end_date']