# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-14 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Storenvy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField()),
                ('store_name', models.CharField(max_length=255)),
                ('sale_today', models.IntegerField(default='0')),
                ('sale_all', models.IntegerField()),
            ],
            options={
                'db_table': 'Storenvy',
            },
        ),
    ]
