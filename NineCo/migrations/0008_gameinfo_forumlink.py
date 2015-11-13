# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NineCo', '0007_auto_20151105_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameinfo',
            name='forumLink',
            field=models.CharField(default='#', blank=True, verbose_name='游戏论坛地址', max_length=50),
        ),
    ]
