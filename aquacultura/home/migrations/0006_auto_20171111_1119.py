# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-11 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_portifolio_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portifolio',
            name='main_image',
            field=models.ImageField(default="{% static'images/port1.png' %}", upload_to='portifolio/images', verbose_name='Imagem'),
        ),
    ]
