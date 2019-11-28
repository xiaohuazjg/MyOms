# -*- coding: utf-8 -*-
# author: itimor

import os
DEBUG = False
TIME_ZONE = 'Asia/Shanghai'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'oms',
        'USER': 'oms',
        'PASSWORD': 'jjyy',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

# 使用ldap认证
AUTHENTICATION_BACKENDS = ("django_python3_ldap.auth.LDAPBackend",)
LDAP_AUTH_URL = "ldap://192.168.6.101:389"
LDAP_AUTH_SEARCH_BASE = "ou=AllUser,dc=oms,dc=com"
LDAP_AUTH_CONNECTION_USERNAME = r'oms\admin'
LDAP_AUTH_CONNECTION_PASSWORD = r'jjyy'

# # Redis
# REDIS_OPTIONS = {
#     'HOST': '127.0.0.1',
#     'PORT': 6379,
#     'DB': 0
# }
# USE_REDIS = True
# # Channel settings
# CHANNEL_LAYERS = {
#     "default": {
#         # 'BACKEND': 'asgiref.inmemory.ChannelLayer',    #如果使用这个，消息变多时，会读不出来
#          "BACKEND": "asgi_redis.RedisChannelLayer",
#          "CONFIG": {
#              "hosts": ['redis://{}:{}'.format(REDIS_OPTIONS['HOST'],
#                                               REDIS_OPTIONS['PORT'])]
#          },
#         "ROUTING": "omsBackend.routing.channel_routing"
#     }
# }

# email账号
MAIL_ACOUNT = {
    "mail_host": "mail@oms.com",
    "mail_user": "admin@oms.com",
    "mail_pass": "jjyy",
    "mail_postfix": "oms.com",
}

# 登录skype
from skpy import Skype

# skype账号
SK_ACOUNT = {
    'sk_user': 'admin@oms.com',
    'sk_pass': 'jjyy'
}
SK = Skype(SK_ACOUNT["sk_user"], SK_ACOUNT["sk_pass"])
#SK = 'skype'

REDIS_URL = 'redis://127.0.0.1:6379/'
# celery配置
CELERY_BROKER_URL = REDIS_URL + '0'

# celery结果返回，可用于跟踪结果
CELERY_RESULT_BACKEND = 'django-db'

# celery内容等消息的格式设置
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

# celery时区设置，使用settings中TIME_ZONE同样的时区
CELERY_TIMEZONE = TIME_ZONE

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL + '1',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# saltapi
salt_info = {
    "url": "http://salt.oms.com/api/",
    "username": "saltapi",
    "password": "saltapi"
}

from salts.saltapi import SaltAPI

sapi = SaltAPI(url=salt_info["url"], username=salt_info["username"], password=salt_info["password"])

from zbmanager.zabbix_api import ZabbixApi

zabbix_info = {
    'apiurl': 'http://zabbix.oms.com/api_jsonrpc.php',
    'username': 'admin',
    'password': 'zabbix'
}

zapi = ZabbixApi(zabbix_info["apiurl"], zabbix_info["username"], zabbix_info["password"])
zapi.login()