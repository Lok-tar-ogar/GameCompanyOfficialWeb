# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NineCo', '0008_gameinfo_forumlink'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsOfBus',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('newsTitle', models.CharField(max_length=50, verbose_name='业务标题')),
                ('newsDetail', models.TextField(max_length=5000, verbose_name='业务详情')),
                ('imgShow', models.FileField(blank=True, null=True, upload_to='img/', verbose_name='展示业务咨询页面的图片')),
                ('upLoadImg', models.FileField(blank=True, null=True, upload_to='img/', verbose_name='上传新闻中的图片，引用图片请采用"/static/img/xxx.xx"格式')),
                ('viewedTimes', models.IntegerField(verbose_name='浏览次数')),
                ('dimDate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-dimDate'],
                'verbose_name': '文章',
            },
        ),
        migrations.RemoveField(
            model_name='gameinfo',
            name='forumLink',
        ),
        migrations.AddField(
            model_name='gameinfo',
            name='imgShow',
            field=models.FileField(blank=True, null=True, upload_to='img/', verbose_name='游戏中心展示（用于展示在首页和游戏列表的图）'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='Image',
            field=models.FileField(upload_to='img/', verbose_name='图片（1920*500）'),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='imgContent1',
            field=models.FileField(blank=True, null=True, upload_to='img/', verbose_name='图片介绍1（296*524）'),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='imgContent2',
            field=models.FileField(blank=True, null=True, upload_to='img/', verbose_name='图片介绍2（同上）'),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='imgUrl',
            field=models.FileField(upload_to='img/', verbose_name='主要图片（100*100）'),
        ),
    ]
