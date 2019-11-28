# -*- coding: utf-8 -*-
# author: itimor

from rest_framework.decorators import api_view
from rest_framework.response import Response
from omsBackend.settings import sapi
from salts.models import SaltState, StateJob, SaltStateGroup, SaltServer
from salts.serializers import SaltStateSerializer, StateJobSerializer, SaltStateGroupSerializer, SaltServerSerializer
from hosts.models import Host
from records.models import Record
import json_tools
from utils.tools import removeNone
from rest_framework import viewsets
import json


class SaltStateViewSet(viewsets.ModelViewSet):
    queryset = SaltState.objects.all()
    serializer_class = SaltStateSerializer
    filter_fields = ['name', 'group__name']


class SaltServerViewSet(viewsets.ModelViewSet):
    queryset = SaltServer.objects.all()
    serializer_class = SaltServerSerializer
    filter_fields = ['name']


@api_view()
def get_all_key(request):
    data = sapi.list_key()
    count = len(data)
    return Response({"results": data, "count": count})


@api_view(['POST'])
def cmdrun(request):
    hosts = request.data["hosts"]
    cmd = request.data["cmd"]
    data = sapi.remote_cmd(tgt=hosts, arg=cmd)
    count = len(data)
    return Response({"results": data, "count": count})


@api_view()
def get_cmd_result(request, jid):
    data = sapi.get_cmd_result(jid)
    count = len(data)
    return Response({"results": data, "count": count})


@api_view()
def sync_remote_server(request, method):
    tgt = sapi.minions_status()['up']
    arg = ['osfinger', 'ipv4', 'cpu_model', 'num_cpus', 'memory_info', 'disk_info']
    data = sapi.sync_remote_server(tgt=tgt, arg=arg)
    count = len(data)
    update_list = []
    no_update_list = []
    for k, v in data[0].items():
        host_info = {
            'hostname': k,
            'os': v['osfinger'],
            'cpu': '{} * {}'.format(v['cpu_model'], v['num_cpus']),
            'memory': v['memory_info'],
            'disk': '|'.join(v['disk_info']),
            'ip': '|'.join(v['ipv4'])
        }

        if method == 'create':
            try:
                obj = Host.objects.get(hostname=k)
            except Host.DoesNotExist:
                obj = Host(**host_info)
                obj.save()
                # records
                Record.objects.create(
                    name='hosts',
                    asset=k,
                    type=1,
                    method='create',
                    before='{}',
                    after=host_info,
                    create_user='auto'
                )
        else:
            try:
                obj = Host.objects.filter(hostname=k)
                obj_info = {
                    'hostname': k,
                    'os': obj[0].os,
                    'cpu': obj[0].cpu,
                    'memory': obj[0].memory,
                    'disk': obj[0].disk,
                    'ip': obj[0].ip
                }

                diff = removeNone(json_tools.diff(obj_info, host_info))
                if diff:
                    obj.update(**host_info)
                    # records
                    Record.objects.create(
                        name='hosts',
                        asset=k,
                        type=1,
                        method='update',
                        before=obj_info,
                        after=host_info,
                        diff=diff,
                        create_user='auto'
                    )
                    update_list.append(k)
                else:
                    no_update_list.append(k)

            except Host.DoesNotExist:
                print("%s is not exist" % k)
    print("update_list: %s" % update_list)
    print("no_update_list: %s" % no_update_list)

    return Response({"results": data, "count": count})


@api_view()
def get_state_bygroup(request):
    from operator import itemgetter
    from itertools import groupby
    if request.method == 'GET':
        queryset = SaltState.objects.all()
        rows = SaltStateSerializer(queryset,  context={'request': request}, many=True).data
        rows.sort(key=itemgetter('group'))
        results = []
        for group, items in groupby(rows, key=itemgetter('group')):
            q = dict()
            q['name'] = group
            q['state'] = []
            for i in items:
                q['state'].append(i)
            results.append(q)
        return Response(results)


class SaltStateGroupViewSet(viewsets.ModelViewSet):
    queryset = SaltStateGroup.objects.all()
    serializer_class = SaltStateGroupSerializer
    filter_fields = ['name']


class StateJobViewSet(viewsets.ModelViewSet):
    queryset = StateJob.objects.all().order_by('-create_time')
    serializer_class = StateJobSerializer
    search_fields = ['statejob__name', 'status']


@api_view()
def update_states_status(request):
    try:
        jobs = StateJob.objects.filter(status='deploy')
        count = len(jobs)
        for job in jobs:
            j_id = job.j_id
            j = StateJob.objects.get(j_id=j_id)
            job_status = sapi.check_job(j_id)
            print(list(set(job_status.values()))[0])
            try:
                if list(set(job_status.values()))[0]:
                    results = sapi.get_state_result(j_id)
                    j.result = json.dumps(results)
                    result_status = []
                    for oo in results.values():
                        for xx in oo.values():
                            result_status.append(xx['result'])
                    if False in result_status:
                        j.status = 'failed'
                    else:
                        j.status = 'success'
                    j.done = True
                else:
                    j.status = 'deploy'
            except Exception as e:
                print(e)
                pass
            j.save()
        return Response({"results": 'success', "count": count})
    except Exception as e:
        return Response({"results": 'tnnd', "count": 1024})
