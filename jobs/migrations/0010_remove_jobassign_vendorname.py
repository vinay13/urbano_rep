# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20160121_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobassign',
            name='vendorname',
        ),
    ]
