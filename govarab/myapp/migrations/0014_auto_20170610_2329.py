# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-10 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20170610_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealership',
            name='type',
            field=models.CharField(choices=[(1, '\u0646\u0645\u0627\u06cc\u0646\u062f\u06af\u0627\u0646 \u0641\u0631\u0648\u0634'), (2, '\u0639\u0627\u0645\u0644\u06cc\u0646 \u0641\u0631\u0648\u0634')], max_length=30, verbose_name='\u0646\u0648\u0639'),
        ),
    ]