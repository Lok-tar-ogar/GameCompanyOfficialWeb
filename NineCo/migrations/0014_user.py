# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NineCo', '0013_auto_20151210_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('username', models.CharField(verbose_name='用户名', max_length=50)),
                ('psd', models.CharField(verbose_name='密码', max_length=50)),
                ('mail', models.EmailField(verbose_name='电子邮件', max_length=500)),
            ],
            options={
                'verbose_name': '用户信息',
            },
        ),
    ]
