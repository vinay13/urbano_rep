# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('fname', models.CharField(max_length=128, default='a')),
                ('lname', models.CharField(max_length=128, default='b')),
                ('DOB', models.CharField(max_length=128, default='c')),
                ('contactno', models.IntegerField(default='+91')),
                ('city', models.CharField(max_length=128, default='JBP')),
                ('state', models.CharField(max_length=128, default='MP')),
                ('landmark', models.CharField(max_length=128, default='e')),
                ('address', models.CharField(max_length=128, default='f')),
                ('pincode', models.IntegerField(default='288412')),
            ],
        ),
    ]
