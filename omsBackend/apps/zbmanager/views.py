# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import viewsets
from rest_framework.response import Response
from zbmanager.serializers import ZbHostSerializer, ZbHostGroupSerializer, ZbTemplateSerializer
from omsBackend.settings import zapi


class ZbHostViewSet(viewsets.ViewSet):
    serializer_class = ZbHostSerializer

    def list(self, request):
        limit = int(request.GET.get('limit', 10))
        offset = int(request.GET.get('offset', 0))
        search = request.GET.get('search', None)
        query = zapi.get_hosts(search=search)
        serializer = ZbHostSerializer(query, many=True)
        data = dict()
        data['count'] = len(serializer.data)
        data['results'] = [serializer.data[i:i + limit] for i in range(0, len(serializer.data), limit)][offset]
        return Response(data)

    def post(self, request):
        if request.data['action'] == 'create':
            hostnames = request.data['hostnames']
            hostgroups = request.data['hostgroups']
            templates = request.data['templates']
            results = []
            for hostName in hostnames:
                req = zapi.create_host(hostName, hostgroups, templates)
                try:
                    results.append({"title": hostName, "type": "error", "message": req["message"]})
                except:
                    results.append({"title": hostName, "type": "success", "message": req})
            return Response(results)
        if request.data['action'] == 'update':
            hostId = request.data['hostid']
            hostName = request.data['host']
            hostgroups = request.data['hostgroups']
            req = zapi.update_host(hostId, hostName, hostgroups)
            try:
                results = [{"title": hostName, "type": "error", "message": req["data"]}]
            except:
                results = [{"title": hostName, "type": "success", "message": req}]
            return Response(results)
        if request.data['action'] == 'delete':
            hostIds = [request.data['hostid']]
            hostName = request.data['host']
            req = zapi.delete_host(hostIds)
            try:
                results = [{"title": hostName, "type": "error", "message": req["message"]}]
            except:
                results = [{"title": hostName, "type": "success", "message": req}]
            return Response(results)


class ZbHostGroupViewSet(viewsets.ViewSet):
    serializer_class = ZbHostGroupSerializer

    def list(self, request):
        query = zapi.get_hostgroups()
        serializer = ZbHostGroupSerializer(query, many=True)
        # limit = request.GET.get('limit', 10)
        # offset = request.GET.get('offset', 0)
        # data = dict()
        # data['count'] = len(serializer.data)
        # data['results'] = [serializer.data[i:i + int(limit)] for i in range(0, len(serializer.data), int(limit))][
        #     int(offset)]
        return Response(serializer.data)


class ZbTemplateViewSet(viewsets.ViewSet):
    serializer_class = ZbTemplateSerializer

    def list(self, request):
        query = zapi.get_templetes()
        serializer = ZbTemplateSerializer(query, many=True)
        return Response(serializer.data)
