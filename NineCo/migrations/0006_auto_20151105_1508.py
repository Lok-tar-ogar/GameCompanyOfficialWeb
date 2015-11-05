# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NineCo', '0005_auto_20151104_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameinfo',
            name='QRimg',
            field=models.FileField(blank=True, upload_to='NineCo/static/img/', verbose_name='上传二维码图片', null=True),
        ),
        migrations.AddField(
            model_name='gameinfo',
            name='gamesize',
            field=models.CharField(blank=True, max_length=50, verbose_name='游戏大小', default='30MB'),
        ),
        migrations.AddField(
            model_name='gameinfo',
            name='imgContent1',
            field=models.FileField(blank=True, upload_to='NineCo/static/img/', verbose_name='图片介绍1', null=True),
        ),
        migrations.AddField(
            model_name='gameinfo',
            name='imgContent2',
            field=models.FileField(blank=True, upload_to='NineCo/static/img/', verbose_name='图片介绍2', null=True),
        ),
        migrations.AddField(
            model_name='gameinfo',
            name='imgContent3',
            field=models.FileField(blank=True, upload_to='NineCo/static/img/', verbose_name='图片介绍3', null=True),
        ),
        migrations.AddField(
            model_name='gameinfo',
            name='version',
            field=models.CharField(blank=True, max_length=50, verbose_name='游戏版本', default='#'),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='Url',
            field=models.FileField(blank=True, upload_to='NineCo/static/apps/', verbose_name='上传APP', null=True),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='imgUrl',
            field=models.FileField(upload_to='NineCo/static/img/', verbose_name='主要图片'),
        ),
        migrations.AlterField(
            model_name='news',
            name='upLoadImg',
            field=models.FileField(blank=True, upload_to='NineCo/static/img/', verbose_name='上传新闻中的图片，引用图片请采用"/static/img/xxx.xx"格式', null=True),
        ),
    ]
