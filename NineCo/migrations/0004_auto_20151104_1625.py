# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NineCo', '0003_auto_20151104_1546'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAdmin',
        ),
        migrations.AlterModelOptions(
            name='carousel',
            options={'ordering': ['-dimDate'], 'verbose_name': '轮播管理'},
        ),
        migrations.AlterModelOptions(
            name='classification',
            options={'verbose_name': '招聘类别'},
        ),
        migrations.AlterModelOptions(
            name='gameclass',
            options={'verbose_name': '游戏类别'},
        ),
        migrations.AlterModelOptions(
            name='gameinfo',
            options={'ordering': ['-dimDate'], 'verbose_name': '游戏信息'},
        ),
        migrations.AlterModelOptions(
            name='jobsinfo',
            options={'ordering': ['-dimDate'], 'verbose_name': '招聘信息'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-dimDate'], 'verbose_name': '文章'},
        ),
        migrations.AlterField(
            model_name='carousel',
            name='Caption',
            field=models.CharField(blank=True, max_length=500, verbose_name='子标题', null=True),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='Image',
            field=models.FileField(verbose_name='图片', upload_to='NineCo/static/img/'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='Linkto',
            field=models.CharField(blank=True, max_length=50, verbose_name='链接地址（可为空）'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='Title',
            field=models.CharField(max_length=50, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='classification',
            name='name',
            field=models.CharField(max_length=25, verbose_name='分类名'),
        ),
        migrations.AlterField(
            model_name='gameclass',
            name='name',
            field=models.CharField(max_length=50, verbose_name='分类名'),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='Url',
            field=models.CharField(blank=True, max_length=100, verbose_name='下载地址', null=True),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='content',
            field=models.TextField(blank=True, max_length=4000, verbose_name='详细介绍', null=True),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='imgUrl',
            field=models.FileField(verbose_name='图片', upload_to='NineCo/static/img/'),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='name',
            field=models.CharField(max_length=50, verbose_name='游戏名'),
        ),
        migrations.AlterField(
            model_name='jobsinfo',
            name='jobDetail',
            field=models.TextField(max_length=2000, verbose_name='职位描述'),
        ),
        migrations.AlterField(
            model_name='jobsinfo',
            name='jobTitle',
            field=models.CharField(max_length=50, verbose_name='职位名'),
        ),
        migrations.AlterField(
            model_name='jobsinfo',
            name='status',
            field=models.CharField(max_length=5, verbose_name='职位状态'),
        ),
        migrations.AlterField(
            model_name='news',
            name='newsDetail',
            field=models.TextField(max_length=5000, verbose_name='新闻详情'),
        ),
        migrations.AlterField(
            model_name='news',
            name='newsTitle',
            field=models.CharField(max_length=50, verbose_name='新闻标题'),
        ),
        migrations.AlterField(
            model_name='news',
            name='viewedTimes',
            field=models.IntegerField(verbose_name='浏览次数'),
        ),
    ]
