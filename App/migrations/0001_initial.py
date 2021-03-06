# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-21 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(blank=True, max_length=16, null=True)),
            ],
            options={
                'db_table': 'Book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=16)),
                ('u_icon', models.ImageField(upload_to='icons')),
            ],
        ),
    ]
