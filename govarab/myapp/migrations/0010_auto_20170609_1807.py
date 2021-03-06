# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-09 13:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20170609_1417'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimage',
            options={'ordering': ['created_at'], 'verbose_name': '\u062a\u0635\u0648\u06cc\u0631 \u0645\u062d\u0635\u0648\u0644', 'verbose_name_plural': '\u062a\u0635\u0648\u06cc\u0631 \u0645\u062d\u0635\u0648\u0644'},
        ),
        migrations.AlterModelOptions(
            name='slidesimages',
            options={'verbose_name': '\u062a\u0635\u0648\u06cc\u0631 \u0628\u0632\u0631\u06af', 'verbose_name_plural': 'Slides Images'},
        ),
        migrations.AddField(
            model_name='team',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='file',
            field=models.FileField(default='', upload_to=b'resume/', verbose_name='CV'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='myapp.Product', verbose_name='\u0645\u062d\u0635\u0648\u0644'),
        ),
    ]
