# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NineCo', '0002_auto_20151103_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameinfo',
            name='content',
            field=models.TextField(blank=True, null=True, max_length=4000),
        ),
        migrations.AlterField(
            model_name='jobsinfo',
            name='jobDetail',
            field=models.TextField(max_length=2000),
        ),
    ]
