# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NineCo', '0012_gameinfo_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsImg',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Image', models.FileField(verbose_name='图片（496*360）', upload_to='img/')),
                ('Linkto', models.CharField(max_length=50, blank=True, verbose_name='链接地址（可为空）')),
                ('dimDate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-dimDate'],
                'verbose_name': '首页图片新闻',
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-dimDate'], 'verbose_name': '新闻'},
        ),
        migrations.AlterModelOptions(
            name='newsofbus',
            options={'ordering': ['-dimDate'], 'verbose_name': '业务咨询'},
        ),
        migrations.AlterField(
            model_name='carousel',
            name='Image',
            field=models.FileField(verbose_name='图片（1920*600）', upload_to='img/'),
        ),
    ]
