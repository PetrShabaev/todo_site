from .models import Project, Todo
from rest_framework.serializers import ModelSerializer, StringRelatedField
from users.serializers import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):

    user = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ('title', 'link', 'user')


class TodoModelSerializer(ModelSerializer):

    user = UserModelSerializer()
    project = StringRelatedField()

    class Meta:
        model = Todo
        fields = ('title', 'body', 'is_active', 'created_at', 'updated_at', 'user', 'project')
