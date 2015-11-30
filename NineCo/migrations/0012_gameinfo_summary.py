# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NineCo', '0011_auto_20151130_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameinfo',
            name='summary',
            field=models.CharField(blank=True, verbose_name='游戏简介', null=True, max_length=300),
        ),
    ]
