# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-11 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20171111_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portifolioimage',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.Portifolio'),
        ),
    ]
