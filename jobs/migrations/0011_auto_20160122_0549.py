# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_remove_jobassign_vendorname'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobassign',
            name='amount',
            field=models.CharField(default=b'0', max_length=124),
        ),
        migrations.AddField(
            model_name='jobassign',
            name='feedback',
            field=models.CharField(default=b'Your feedback here..', max_length=230),
        ),
    ]
