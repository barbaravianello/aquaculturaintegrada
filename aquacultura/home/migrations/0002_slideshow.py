# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-14 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slideshow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('image', models.ImageField(blank=True, null=True, upload_to='slideshow/images', verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Slideshow',
                'verbose_name_plural': 'Slideshow',
                'ordering': ['name'],
            },
        ),
    ]
