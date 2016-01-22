# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_auto_20160122_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobassign',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='jobassign',
            name='payment',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='jobassign',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
