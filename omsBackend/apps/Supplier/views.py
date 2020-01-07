from django.shortcuts import render
from rest_framework import viewsets
from apps.Supplier.models import Supplier
from apps.Supplier.serializers import SupplierSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from apps.Supplier.filters import SupplierFilterBackend
# Create your views here.


class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends = (SupplierFilterBackend, SearchFilter, DjangoFilterBackend)
    filter_fields = ['supplier_no', 'supplier_name', 'supplier_addrss','business_contacts', 'business_contact_number',
                  'technical_contact', 'technical_contact_number', 'service_scope', 'supplier_remarks']
    search_fields = ['supplier_no', 'supplier_name', 'supplier_addrss','business_contacts', 'business_contact_number',
                  'technical_contact', 'technical_contact_number', 'service_scope', 'supplier_remarks']