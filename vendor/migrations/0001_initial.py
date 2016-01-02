# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('firstname', models.CharField(max_length=128, default='firstname')),
                ('lastname', models.CharField(max_length=128, default='lastname')),
                ('profile', models.CharField(max_length=128, default='plumber')),
                ('gender', models.CharField(max_length=128, default='M')),
                ('DOB', models.CharField(max_length=128, default='12-4-1979')),
                ('state', models.CharField(max_length=128, default='MP')),
                ('city', models.CharField(max_length=128, default='jbp')),
                ('address', models.CharField(max_length=128, default='address')),
                ('contactNo', models.IntegerField(default='+91')),
            ],
        ),
    ]
