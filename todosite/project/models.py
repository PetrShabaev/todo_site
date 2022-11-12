from django.db import models
from users.models import User


class Project(models.Model):
    title = models.CharField(verbose_name='Название проекта', max_length=80)
    link = models.URLField(verbose_name='Ссылка на репозиторий', blank=True)
    user = models.ManyToManyField(User, related_name='user')

    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField(verbose_name='Тема заметки', max_length=80)
    body = models.TextField(verbose_name='Текст заметки')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
