from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination



class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer


class ProjectListCreateAPIView(APIView, PageNumberPagination):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    page_size = 10

    def get(self, request, format=None):
        projects = Project.objects.all()
        query_title = request.query_params.get('title', None)
        if query_title:
            projects = projects.filter(title__icontains=query_title.capitalize())
            print(projects)
            result_page = self.paginate_queryset(projects, request, view=self)
            serializer = ProjectModelSerializer(result_page, many=True)
            return self.get_paginated_response(serializer.data)
        result_page = self.paginate_queryset(projects, request, view=self)
        serializer = ProjectModelSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class ProjectRetrievePutDeleteAPIView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request, pk):
        project = Project.objects.get(pk=pk)
        serializer = ProjectModelSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        instance = get_object_or_404(Project, pk=pk)
        serializer = ProjectModelSerializer(data=request.data, instance=instance)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        Project.objects.get(pk=pk).delete()
        return Response()


class ToDoListCreateAPIView(APIView, PageNumberPagination):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    page_size = 20

    def get(self, request, format=None):
        todos = Todo.objects.all()
        query_word = request.query_params.get('project', None)
        if query_word:
            todos = todos.filter(project__title__icontains=query_word.capitalize())
        results = self.paginate_queryset(todos, request, view=self)
        serializer = TodoModelSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoModelSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)


class ToDoRetrievePutDeleteAPIView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        serializer = TodoModelSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        instance = get_object_or_404(Todo, pk=pk)
        serializer = TodoModelSerializer(data=request.data, instance=instance)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        todo.is_active = False
        todo.save()

        return Response(TodoModelSerializer(todo).data)
