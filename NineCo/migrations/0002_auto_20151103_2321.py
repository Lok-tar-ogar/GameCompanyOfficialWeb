# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NineCo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='newsDetail',
            field=models.TextField(max_length=5000),
        ),
    ]
