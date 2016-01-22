# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_auto_20160122_0556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobdetails',
            name='category_name',
        ),
        migrations.RemoveField(
            model_name='jobdetails',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='jobdetails',
            name='subcategory_name',
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='WantedDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='Wantedtimestart',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='createdateTime',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
