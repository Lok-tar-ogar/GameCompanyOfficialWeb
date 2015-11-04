# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NineCo', '0004_auto_20151104_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='upLoadImg',
            field=models.FileField(blank=True, upload_to='NineCo/static/img/', verbose_name='上传新闻中的图片，引用图片请采用"static/img/xxx.xx"格式', null=True),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='Url',
            field=models.FileField(blank=True, upload_to='NineCo/static/img/', verbose_name='上传APP', null=True),
        ),
    ]
