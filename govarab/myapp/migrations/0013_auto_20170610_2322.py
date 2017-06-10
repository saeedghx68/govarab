# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-10 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_dealership'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['created_at'], 'verbose_name': '\u0645\u0642\u0627\u0644\u0647', 'verbose_name_plural': '\u0645\u0642\u0627\u0644\u0627\u062a'},
        ),
        migrations.AlterModelOptions(
            name='dealership',
            options={'ordering': ['name'], 'verbose_name': '\u0646\u0645\u0627\u06cc\u0646\u062f\u06af\u06cc', 'verbose_name_plural': '\u0646\u0645\u0627\u06cc\u0646\u062f\u06af\u06cc \u0647\u0627'},
        ),
        migrations.AlterField(
            model_name='article',
            name='link',
            field=models.URLField(verbose_name='\u0644\u06cc\u0646\u06a9 \u0645\u0646\u0628\u0639'),
        ),
        migrations.AlterField(
            model_name='dealership',
            name='address',
            field=models.CharField(max_length=300, verbose_name='\u0622\u062f\u0631\u0633'),
        ),
        migrations.AlterField(
            model_name='dealership',
            name='address_ar',
            field=models.CharField(max_length=300, null=True, verbose_name='\u0622\u062f\u0631\u0633'),
        ),
        migrations.AlterField(
            model_name='dealership',
            name='address_en',
            field=models.CharField(max_length=300, null=True, verbose_name='\u0622\u062f\u0631\u0633'),
        ),
        migrations.AlterField(
            model_name='dealership',
            name='address_fa',
            field=models.CharField(max_length=300, null=True, verbose_name='\u0622\u062f\u0631\u0633'),
        ),
        migrations.AlterField(
            model_name='dealership',
            name='tel',
            field=models.CharField(max_length=14, verbose_name='\u062a\u0644\u0641\u0646'),
        ),
        migrations.AlterField(
            model_name='dealership',
            name='type',
            field=models.CharField(choices=[('\u0646\u0645\u0627\u06cc\u0646\u062f\u06af\u0627\u0646 \u0641\u0631\u0648\u0634', '\u0646\u0645\u0627\u06cc\u0646\u062f\u06af\u0627\u0646 \u0641\u0631\u0648\u0634'), ('\u0639\u0627\u0645\u0644\u06cc\u0646 \u0641\u0631\u0648\u0634', '\u0639\u0627\u0645\u0644\u06cc\u0646 \u0641\u0631\u0648\u0634')], max_length=30, verbose_name='\u0646\u0648\u0639'),
        ),
        migrations.AlterField(
            model_name='team',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='\u0627\u06cc\u0645\u06cc\u0644'),
        ),
    ]