# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NineCo', '0015_forum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='user',
            field=models.IntegerField(),
        ),
    ]
