# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_remove_jobdetails_invoice_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobassign',
            name='jobid',
            field=models.ForeignKey(to='jobs.JobDetails'),
        ),
        migrations.AlterField(
            model_name='jobassign',
            name='vendorid',
            field=models.ForeignKey(to='vendor.Vendor'),
        ),
    ]
