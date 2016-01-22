# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_auto_20160101_1306'),
        ('jobs', '0007_remove_jobassign_vendorid'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobassign',
            name='vendorid',
            field=models.ForeignKey(blank=True, to='vendor.Vendor', null=True),
        ),
        migrations.AlterField(
            model_name='jobassign',
            name='jobid',
            field=models.ForeignKey(blank=True, to='jobs.JobDetails', null=True),
        ),
    ]
