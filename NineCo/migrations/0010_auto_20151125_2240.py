# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NineCo', '0009_auto_20151124_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameinfo',
            name='forumLink',
            field=models.CharField(verbose_name='论坛链接', null=True, max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='QRimg',
            field=models.FileField(verbose_name='上传二维码图片（120*120）', upload_to='img/', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='imgUrl',
            field=models.FileField(verbose_name='主要图片（120*120）', upload_to='img/'),
        ),
    ]
