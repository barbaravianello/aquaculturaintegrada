# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 18:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20171111_1123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portifolio',
            options={'ordering': ['name'], 'verbose_name': 'Portfólio', 'verbose_name_plural': 'Portfólios'},
        ),
    ]