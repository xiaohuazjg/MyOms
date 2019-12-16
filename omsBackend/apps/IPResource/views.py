from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from apps.IPResource.serializers import IPResourceSerializer
from apps.IPResource.models import IPResource
from apps.IPResource.filters import IPResourceFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class IPResourceViewSet(viewsets.ModelViewSet):
    serializer_class = IPResourceSerializer
    queryset = IPResource.objects.all()
    filter_backends =(DjangoFilterBackend, IPResourceFilterBackend, SearchFilter)
    filter_fields = ["IP_Address", "IP_Mask", "IP_Affiliated_link", "IP_Affiliated_Room",
                     "IP_Status", "IP_Equipment", "IP_User", "IP_Class", "IP_Remarks"]
    search_fields = ["IP_Address", "IP_Mask", "IP_Affiliated_link", "IP_Affiliated_Room",
                     "IP_Status", "IP_Equipment", "IP_User", "IP_Class", "IP_Remarks"]
