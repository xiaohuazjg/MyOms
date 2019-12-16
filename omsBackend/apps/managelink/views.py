from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from apps.managelink.serializers import ManageLinkSerializer
from apps.managelink.models import ManageLink
from apps.managelink.filters import LinkFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class ManageLinkViewSet(viewsets.ModelViewSet):
    serializer_class = ManageLinkSerializer
    filter_backends = (LinkFilterBackend, DjangoFilterBackend, SearchFilter)
    queryset = ManageLink.objects.all()
    filter_fields = ['link_name', 'link_code', 'link_room']
    search_fields = ['link_type', 'link_name']
