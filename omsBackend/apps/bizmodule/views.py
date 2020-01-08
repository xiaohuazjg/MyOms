from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from apps.bizmodule.models import BizModule
from apps.bizmodule.serializers import BizModuleSerializer


class BizModuleViewSet(viewsets.ModelViewSet):
    queryset = BizModule.objects.all()
    serializer_class = BizModuleSerializer
    filter_fields = ['biz_code', 'biz_name', 'parent']
    search_fields = ['biz_code', 'biz_name', 'parent']