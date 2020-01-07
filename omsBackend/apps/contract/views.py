from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from apps.contract.filters import ContractFilterBackend
from apps.contract.models import Contract, ContractExpire
from apps.contract.serializers import ContractSerializer, ContractExpireSerializer
# Create your views here.


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    filter_backends = (ContractFilterBackend, DjangoFilterBackend, SearchFilter)
    filter_fields = ['contract_number', 'contract_name', 'contract_amount', 'contract_signing_date',
                     'contract_start_date', 'contract_end_date', 'contract_term_type', 'contract_product_type',
                     'contract_supplier', 'contract_signed_by', 'contract_remarks']
    search_fields = ['contract_number', 'contract_name', 'contract_amount', 'contract_signing_date',
                     'contract_start_date', 'contract_end_date', 'contract_term_type', 'contract_product_type',
                     'contract_supplier', 'contract_signed_by', 'contract_remarks']


class ContractExpireViewSet(viewsets.ModelViewSet):
    queryset = ContractExpire.objects.all()
    serializer_class = ContractExpireSerializer
