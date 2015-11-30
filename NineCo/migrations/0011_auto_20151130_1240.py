# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NineCo', '0010_auto_20151125_2240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': '业务咨询', 'ordering': ['-dimDate']},
        ),
        migrations.RenameField(
            model_name='news',
            old_name='upLoadImg',
            new_name='upLoadImg1',
        ),
        migrations.AddField(
            model_name='news',
            name='upLoadImg2',
            field=models.FileField(blank=True, null=True, verbose_name='上传新闻中的图片，引用图片请采用"/static/img/xxx.xx"格式', upload_to='img/'),
        ),
        migrations.AddField(
            model_name='news',
            name='upLoadImg3',
            field=models.FileField(blank=True, null=True, verbose_name='上传新闻中的图片，引用图片请采用"/static/img/xxx.xx"格式', upload_to='img/'),
        ),
        migrations.AddField(
            model_name='news',
            name='upLoadImg4',
            field=models.FileField(blank=True, null=True, verbose_name='上传新闻中的图片，引用图片请采用"/static/img/xxx.xx"格式', upload_to='img/'),
        ),
        migrations.AddField(
            model_name='news',
            name='upLoadImg5',
            field=models.FileField(blank=True, null=True, verbose_name='上传新闻中的图片，引用图片请采用"/static/img/xxx.xx"格式', upload_to='img/'),
        ),
        migrations.AddField(
            model_name='newsofbus',
            name='upLoadImg2',
            field=models.FileField(blank=True, null=True, verbose_name='上传新闻中的图片，引用图片请采用"/static/img/xxx.xx"格式', upload_to='img/'),
        ),
        migrations.AddField(
            model_name='newsofbus',
            name='upLoadImg3',
            field=models.FileField(blank=True, null=True, verbose_name='上传新闻中的图片，引用图片请采用"/static/img/xxx.xx"格式', upload_to='img/'),
        ),
        migrations.AddField(
            model_name='newsofbus',
            name='upLoadImg4',
            field=models.FileField(blank=True, null=True, verbose_name='上传新闻中的图片，引用图片请采用"/static/img/xxx.xx"格式', upload_to='img/'),
        ),
        migrations.AddField(
            model_name='newsofbus',
            name='upLoadImg5',
            field=models.FileField(blank=True, null=True, verbose_name='上传新闻中的图片，引用图片请采用"/static/img/xxx.xx"格式', upload_to='img/'),
        ),
    ]
