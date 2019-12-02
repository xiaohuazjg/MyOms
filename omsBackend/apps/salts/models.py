# -*- coding: utf-8 -*-
# author: huashaw

from django.db import models
from apps.users.models import User


class SaltState(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'名称')
    group = models.ForeignKey('SaltStateGroup', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'分组')
    cmd = models.CharField(max_length=100, verbose_name=u'state命令')
    desc = models.TextField(null=True, blank=True, verbose_name=u'备注')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'state服务'
        verbose_name_plural = u'state服务'


class SaltStateGroup(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'名称')
    desc = models.TextField(null=True, blank=True, verbose_name=u'备注')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'state服务组'
        verbose_name_plural = u'state服务组'


RUN_STATUS = {
    "deploy": "执行中",
    "success": "执行成功",
    "failed": "执行失败"
}


class StateJob(models.Model):
    statejob = models.ForeignKey(SaltState, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'state服务')
    j_id = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'任务ID')
    status = models.CharField(choices=RUN_STATUS.items(), default="deploy", max_length=9, verbose_name=u'状态')
    hosts = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'目标主机')
    action_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'操作人')
    result = models.TextField(null=True, blank=True, verbose_name=u'结果')
    done = models.BooleanField(default=False, verbose_name=u'完成')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    def __str__(self):
        return self.j_id

    class Meta:
        verbose_name = u'执行state'
        verbose_name_plural = u'执行state'


class SaltServer(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name=u'名称')
    apiurl = models.CharField(max_length=64, verbose_name=u'api地址')
    user = models.CharField(max_length=64, verbose_name=u'用户名')
    password = models.CharField(max_length=64, verbose_name=u'密码')
    desc = models.TextField(null=True, blank=True, verbose_name=u'备注')

    def __str__(self):
        return self.apiurl

    class Meta:
        verbose_name = 'salt server'
        verbose_name_plural = 'salt server'
