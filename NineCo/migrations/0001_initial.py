# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Image', models.CharField(max_length=50)),
                ('Linkto', models.CharField(max_length=50)),
                ('Caption', models.CharField(max_length=500, null=True, blank=True)),
                ('dimDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='GameClass',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GameInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('imgUrl', models.CharField(max_length=50, blank=True)),
                ('Url', models.CharField(max_length=100, null=True, blank=True)),
                ('content', models.CharField(max_length=4000, null=True, blank=True)),
                ('dimDate', models.DateField(auto_now_add=True)),
                ('gameType', models.ForeignKey(to='NineCo.GameClass')),
            ],
        ),
        migrations.CreateModel(
            name='JobsInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('jobTitle', models.CharField(max_length=50)),
                ('jobDetail', models.CharField(max_length=2000)),
                ('dimDate', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=5)),
                ('classification', models.ForeignKey(to='NineCo.Classification')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('newsTitle', models.CharField(max_length=50)),
                ('newsDetail', models.CharField(max_length=5000)),
                ('viewedTimes', models.IntegerField()),
                ('dimDate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-dimDate'],
            },
        ),
        migrations.CreateModel(
            name='UserAdmin',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('userName', models.CharField(max_length=50)),
                ('userPsd', models.CharField(max_length=50)),
                ('regDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
