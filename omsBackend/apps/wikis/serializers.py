# -*- coding: utf-8 -*-
# author: kiven

from apps.wikis.models import Wiki
from rest_framework import serializers
from apps.users.models import User, Group
from apps.worktickets.models import TicketType


class WikiSerializer(serializers.ModelSerializer):
    create_user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    type = serializers.SlugRelatedField(queryset=TicketType.objects.all(), slug_field='name', allow_null=True)

    class Meta:
        model = Wiki
        fields = ('url', 'id', 'title', 'type', 'content', 'create_user', 'create_time', 'update_time')
