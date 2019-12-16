# -*- coding: utf-8 -*-
# author: huashaw


from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from apps.computer_room.serializers import ComputerRoomSerializer
from apps.computer_room.models import ComputerRoom
from apps.computer_room.filters import ComputerRoomFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class ComputerRoomViewSet(viewsets.ModelViewSet):
    queryset = ComputerRoom.objects.all()
    serializer_class = ComputerRoomSerializer
    filter_backends = (ComputerRoomFilterBackend, DjangoFilterBackend, SearchFilter)
    filter_fields = ['room_name']
    search_fields = ['room_isEnable', 'room_name']

