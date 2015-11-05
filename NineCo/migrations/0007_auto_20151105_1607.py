# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NineCo', '0006_auto_20151105_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='Image',
            field=models.FileField(verbose_name='图片', upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='QRimg',
            field=models.FileField(verbose_name='上传二维码图片', blank=True, upload_to='img/', null=True),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='Url',
            field=models.FileField(verbose_name='上传APP', blank=True, upload_to='apps/', null=True),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='imgContent1',
            field=models.FileField(verbose_name='图片介绍1', blank=True, upload_to='img/', null=True),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='imgContent2',
            field=models.FileField(verbose_name='图片介绍2', blank=True, upload_to='img/', null=True),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='imgContent3',
            field=models.FileField(verbose_name='图片介绍3', blank=True, upload_to='img/', null=True),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='imgUrl',
            field=models.FileField(verbose_name='主要图片', upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='upLoadImg',
            field=models.FileField(verbose_name='上传新闻中的图片，引用图片请采用"/static/img/xxx.xx"格式', blank=True, upload_to='img/', null=True),
        ),
    ]
