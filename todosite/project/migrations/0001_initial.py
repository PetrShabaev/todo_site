# Generated by Django 4.1.2 on 2022-11-12 19:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Название проекта')),
                ('link', models.URLField(blank=True, verbose_name='Ссылка на репозеторий')),
                ('user', models.ManyToManyField(related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
