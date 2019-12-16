# -*- coding: utf-8 -*-
# author: kiven


from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token
from rest_auth.views import PasswordChangeView
from django.views.generic.base import TemplateView
from omsBackend import settings
from omsBackend.routerApi import router
from apps.perms.views import routers
from apps.jobs.views import update_jobs_status
from apps.salts.views import update_states_status, get_state_bygroup

# version模块自动注册需要版本控制的 Model


urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [

    url(r'^api/', include(router.urls)),
    url(r'^api/routers/', routers, name="myrouter"),
    url(r'^api/update_jobs_status/', update_jobs_status, name="update_jobs_status"),
    url(r'^api/update_states_status/', update_states_status, name="update_states_status"),
    url(r'^api/get_state_bygroup/', get_state_bygroup, name="get_state_bygroup"),

    # salt
    url(r'^api/salts/', include('apps.salts.urls')),

    # 用户认证
    url(r'^api/changepasswd/', PasswordChangeView.as_view(), name='changepasswd'),
    url(r'^api/api-token-auth/', obtain_jwt_token, name='rest_framework_token'),
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'', TemplateView.as_view(template_name="index.html")),
]
