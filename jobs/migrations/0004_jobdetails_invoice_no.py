# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20160119_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdetails',
            name='invoice_no',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
