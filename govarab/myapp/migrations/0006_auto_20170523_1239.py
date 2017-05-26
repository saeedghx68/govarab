# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-23 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_team_post_fa'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='question')),
                ('answer', models.TextField(verbose_name='answer')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'FAQs',
                'verbose_name': 'FAQ',
                'ordering': ['updated_at'],
            },
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Product Category', 'verbose_name_plural': 'Product Category'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='model',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specification',
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='img',
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='text',
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='product',
            name='big_img',
            field=models.ImageField(default='images/products/defaults.jpg', help_text='size(570px * 453px)', upload_to='images/products/', verbose_name='large image'),
        ),
        migrations.AddField(
            model_name='product',
            name='small_img',
            field=models.ImageField(default='images/products/defaults.jpg', help_text='size(370px * 294px)', upload_to='images/products/', verbose_name='small image'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]