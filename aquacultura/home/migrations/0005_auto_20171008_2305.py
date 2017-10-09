# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 02:05
from __future__ import unicode_literals

from django.db import migrations
import fontawesome.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_portifolio_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
        migrations.AddField(
            model_name='service',
            name='icon',
            field=fontawesome.fields.IconField(blank=True, max_length=60),
        ),
    ]