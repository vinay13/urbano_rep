# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subCat_name', models.CharField(max_length=128, default='tv repair')),
                ('metatags', models.CharField(max_length=128, default='tcc')),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='subcategoryName',
        ),
        migrations.AddField(
            model_name='category',
            name='cat_order',
            field=models.CharField(max_length=128, default='cat_order'),
        ),
        migrations.AddField(
            model_name='category',
            name='keywords',
            field=models.CharField(max_length=128, default='keywords'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='cat_id',
            field=models.ForeignKey(to='category.Category'),
        ),
    ]
