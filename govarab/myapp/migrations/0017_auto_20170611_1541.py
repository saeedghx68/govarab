# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-11 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20170611_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='reference_title_ar',
            field=models.CharField(default=b'', max_length=300, null=True, verbose_name='Reference title'),
        ),
        migrations.AddField(
            model_name='article',
            name='reference_title_en',
            field=models.CharField(default=b'', max_length=300, null=True, verbose_name='Reference title'),
        ),
        migrations.AddField(
            model_name='article',
            name='reference_title_fa',
            field=models.CharField(default=b'', max_length=300, null=True, verbose_name='Reference title'),
        ),
    ]