# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-22 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApplication', '0006_auto_20160921_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_msg', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Other',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='category_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BlogApplication.Category'),
        ),
    ]
