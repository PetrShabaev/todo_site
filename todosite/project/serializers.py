from .models import Project, Todo
from rest_framework.serializers import ModelSerializer, StringRelatedField, SlugRelatedField
from users.serializers import UserModelSerializer
from users.models import User


class ProjectModelSerializer(ModelSerializer):

    user = SlugRelatedField(many=True, queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Project
        fields = ('title', 'link', 'user')


class TodoModelSerializer(ModelSerializer):

    user = SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    project = SlugRelatedField(queryset=Project.objects.all(), slug_field='title')

    class Meta:
        model = Todo
        fields = ('title', 'body', 'is_active', 'created_at', 'updated_at', 'user', 'project')
