# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-24 17:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApplication', '0008_auto_20160922_1038'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Other',
        ),
        migrations.AlterField(
            model_name='post',
            name='category_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BlogApplication.Category'),
        ),
    ]
