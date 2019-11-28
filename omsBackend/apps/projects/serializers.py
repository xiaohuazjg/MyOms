# -*- coding: utf-8 -*-
# author: kiven

from projects.models import Project, ProjectComment, ProjectEnclosure, ProjectType, BugManager, TestManager, \
    DemandManager, DemandEnclosure, ProjectComplete
from rest_framework import serializers
from users.models import User, Group
from tools.models import Upload


class ProjectSerializer(serializers.ModelSerializer):
    demand = serializers.SlugRelatedField(queryset=DemandManager.objects.all(), slug_field='pid')
    type = serializers.SlugRelatedField(queryset=ProjectType.objects.all(), slug_field='name', allow_null=True)
    create_user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    action_user = serializers.SlugRelatedField(many=True, queryset=User.objects.all(), slug_field='username',
                                               allow_null=True)
    follow_user = serializers.SlugRelatedField(many=True, queryset=User.objects.all(), slug_field='username',
                                               allow_null=True)
    user_complete = serializers.SerializerMethodField()

    def get_user_complete(self, obj):
        users = obj.action_user.all()
        user_completes = []
        sum = 0
        for user in users:
            try:
                o = ProjectComplete.objects.get(project=obj.id, user=user.id)
                complete = o.complete
            except:
                complete = 0
                o = ProjectComplete.objects.create(project=obj, user=user, complete=complete)

            sum += complete
            user_completes.append({'id': o.id, 'action_user': user.username, 'complete': complete})
        b = Project.objects.get(id=obj.id)

        if b.status == '7':
            b.task_complete = 100
            b.test_complete = 100
        else:
            b.task_complete = int(sum / len(users))
            if b.task_complete == 100:
                if int(b.status) < 3:
                    b.status = 3

                if 0 < b.test_complete < 100:
                    b.status = 4
                elif b.test_complete == 100:
                    if int(b.status) < 6:
                        b.status = 6
            elif b.task_complete == 0:
                b.test_complete = 0
                b.status = 1
            else:
                b.test_complete = 0
                b.status = 2

        b.save()
        return user_completes

    class Meta:
        model = Project
        fields = (
            'url', 'id', 'demand', 'pid', 'name', 'type', 'level', 'status', 'task_complete', 'test_complete',
            'content', 'create_user', 'test_user', 'action_user', 'follow_user', 'from_user', 'create_date',
            'update_date', 'create_time', 'update_time', 'start_time', 'end_time', 'is_public', 'user_complete')


class ProjectCompleteSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = ProjectComplete
        fields = ('url', 'id', 'project', 'complete', 'user')


class ProjectCommentSerializer(serializers.ModelSerializer):
    create_user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = ProjectComment
        fields = ('url', 'id', 'project', 'content', 'create_user', 'create_time')


class ProjectEnclosureSerializer(serializers.ModelSerializer):
    create_user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    file = serializers.SlugRelatedField(queryset=Upload.objects.all(), slug_field='filepath')

    class Meta:
        model = ProjectEnclosure
        fields = ('url', 'id', 'project', 'file', 'create_user', 'create_time')


class ProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectType
        fields = ('url', 'id', 'name', 'desc')


class BugManagerSerializer(serializers.ModelSerializer):
    project = serializers.SlugRelatedField(queryset=Project.objects.all(), slug_field='pid', allow_null=True)
    test_user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    action_user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = BugManager
        fields = (
            'url', 'id', 'project', 'test', 'name', 'desc', 'degree', 'nice', 'status', 'test_user', 'action_user',
            'test_time', 'end_time', 'create_time')


class TestManagerSerializer(serializers.ModelSerializer):
    project = serializers.SlugRelatedField(queryset=Project.objects.all(), slug_field='pid', allow_null=True)
    test_user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    action_user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = TestManager
        fields = (
            'url', 'id', 'project', 'name', 'expect_result', 'actual_result', 'status', 'test_user', 'action_user',
            'test_time', 'create_time')


class DemandManagerSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(queryset=ProjectType.objects.all(), slug_field='name', allow_null=True)
    create_user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = DemandManager
        fields = (
            'url', 'id', 'pid', 'name', 'type', 'content', 'create_user', 'status', 'create_time', 'end_time')


class DemandEnclosureSerializer(serializers.ModelSerializer):
    create_user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    file = serializers.SlugRelatedField(queryset=Upload.objects.all(), slug_field='filepath')

    class Meta:
        model = DemandEnclosure
        fields = ('url', 'id', 'project', 'file', 'create_user', 'create_time')
