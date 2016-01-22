# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20160121_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobassign',
            name='vendorname',
            field=models.CharField(default=b'argss', max_length=128),
        ),
    ]
