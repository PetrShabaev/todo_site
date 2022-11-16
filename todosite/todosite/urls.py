"""todosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users import views
from project.views import *

router = DefaultRouter()
router.register('users', views.UserModelViewSet)
router.register('projects',  ProjectModelViewSet)
router.register('todos',  TodoModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/userapilist/', views.UserListAPIView.as_view()),
    path('api/userdetail/<int:pk>/', views.UserDetailPutView.as_view()),
    path('api/projectlist/', ProjectListCreateAPIView.as_view()),
    path('api/projectlist/<str:title>/', ProjectListCreateAPIView.as_view()),
    path('api/projectdetail/<int:pk>/', ProjectRetrievePutDeleteAPIView.as_view()),
    path('api/todoapilist/', ToDoListCreateAPIView.as_view()),
    path('api/tododetail/<int:pk>/', ToDoRetrievePutDeleteAPIView.as_view()),
    path('api/todoapilist/<str:project>/', ToDoListCreateAPIView.as_view()),
]
