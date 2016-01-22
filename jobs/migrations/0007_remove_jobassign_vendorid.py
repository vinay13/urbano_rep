# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20160121_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobassign',
            name='vendorid',
        ),
    ]
