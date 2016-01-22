# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20160101_1026'),
        ('customer', '0001_initial'),
        ('jobs', '0011_auto_20160122_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdetails',
            name='category_id',
            field=models.ForeignKey(blank=True, to='category.Category', null=True),
        ),
        migrations.AddField(
            model_name='jobdetails',
            name='customer_id',
            field=models.ForeignKey(blank=True, to='customer.Customer', null=True),
        ),
        migrations.AddField(
            model_name='jobdetails',
            name='subcategory_id',
            field=models.ForeignKey(blank=True, to='category.SubCategory', null=True),
        ),
    ]
