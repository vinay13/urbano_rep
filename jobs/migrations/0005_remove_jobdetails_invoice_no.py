# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_jobdetails_invoice_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobdetails',
            name='invoice_no',
        ),
    ]
