# -*- coding: utf-8 -*-
# author: kiven

from django.conf.urls import url
from salts import views

urlpatterns = [
    url(r'^get_all_key/', views.get_all_key),
    url(r'^cmdrun/', views.cmdrun),
    url(r'^get_cmd_result/(?P<jid>\w+)', views.get_cmd_result),
    url(r'^sync_remote_server/(?P<method>\w+)', views.sync_remote_server),
]
