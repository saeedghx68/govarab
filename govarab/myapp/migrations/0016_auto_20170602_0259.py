# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-01 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20170601_1417'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'ordering': ['updated_at'], 'verbose_name': '\u0633\u0624\u0627\u0644\u0627\u062a \u0645\u062a\u062f\u0627\u0648\u0644', 'verbose_name_plural': '\u0633\u0624\u0627\u0644\u0627\u062a \u0645\u062a\u062f\u0627\u0648\u0644'},
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(verbose_name='\u067e\u0627\u0633\u062e'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_ar',
            field=models.TextField(null=True, verbose_name='\u067e\u0627\u0633\u062e'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_en',
            field=models.TextField(null=True, verbose_name='\u067e\u0627\u0633\u062e'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_fa',
            field=models.TextField(null=True, verbose_name='\u067e\u0627\u0633\u062e'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.TextField(verbose_name='\u067e\u0631\u0633\u0634'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_ar',
            field=models.TextField(null=True, verbose_name='\u067e\u0631\u0633\u0634'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_en',
            field=models.TextField(null=True, verbose_name='\u067e\u0631\u0633\u0634'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_fa',
            field=models.TextField(null=True, verbose_name='\u067e\u0631\u0633\u0634'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=b'', verbose_name='\u062a\u0648\u0636\u06cc\u062d\u0627\u062a \u0645\u062d\u0635\u0648\u0644'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_ar',
            field=models.TextField(default=b'', null=True, verbose_name='\u062a\u0648\u0636\u06cc\u062d\u0627\u062a \u0645\u062d\u0635\u0648\u0644'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_en',
            field=models.TextField(default=b'', null=True, verbose_name='\u062a\u0648\u0636\u06cc\u062d\u0627\u062a \u0645\u062d\u0635\u0648\u0644'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_fa',
            field=models.TextField(default=b'', null=True, verbose_name='\u062a\u0648\u0636\u06cc\u062d\u0627\u062a \u0645\u062d\u0635\u0648\u0644'),
        ),
    ]