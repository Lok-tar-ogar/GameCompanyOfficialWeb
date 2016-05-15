# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NineCo', '0016_auto_20160515_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.TextField(verbose_name='内容', max_length=5000)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('forum', models.IntegerField()),
                ('response_comment', models.IntegerField()),
            ],
            options={
                'verbose_name': '评论信息',
            },
        ),
    ]
