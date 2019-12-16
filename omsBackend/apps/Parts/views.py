from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from apps.Parts.filters import PartsFilterBackend
from rest_framework import viewsets
from apps.Parts.serializers import PartsSerializer
from apps.Parts.models import Parts


class PartsViewSet(viewsets.ModelViewSet):
    serializer_class = PartsSerializer
    filter_backends = (PartsFilterBackend, SearchFilter, DjangoFilterBackend)
    queryset = Parts.objects.all()
    filter_fields = ['parts_code', 'parts_type', 'parts_details', 'parts_specs', 'parts_supplier', 'parts_brand',
                  'parts_asset_no', 'parts_status', 'parts_date', 'parts_remarks']

    search_fields = ['parts_code', 'parts_type', 'parts_details', 'parts_specs', 'parts_supplier', 'parts_brand',
                  'parts_asset_no', 'parts_status', 'parts_date', 'parts_remarks']
