# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_jobassign_vendorname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobassign',
            name='payment',
            field=models.CharField(default=b'unpaid', max_length=128),
        ),
    ]
