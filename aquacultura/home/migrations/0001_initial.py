# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('description', models.TextField(blank=True, max_length=220, verbose_name='Descrição ')),
                ('image', models.ImageField(blank=True, null=True, upload_to='team/images', verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Equipe',
                'verbose_name_plural': 'Equipe',
                'ordering': ['name'],
            },
        ),
    ]
