# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NineCo', '0014_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', models.TextField(max_length=5000, verbose_name='内容')),
                ('status', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to='NineCo.User')),
            ],
            options={
                'verbose_name': '论坛文章',
            },
        ),
    ]
