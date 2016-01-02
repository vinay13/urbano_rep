# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='firstname',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='lastname',
            new_name='lname',
        ),
    ]
