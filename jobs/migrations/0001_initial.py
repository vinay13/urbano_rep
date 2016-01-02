# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobAssign',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('jobid', models.CharField(default='0', max_length=128)),
                ('vendorid', models.CharField(default='0', max_length=128)),
                ('datetime', models.CharField(default='20-01-2015', max_length=128)),
                ('payment', models.CharField(default='not paid', max_length=128)),
                ('status', models.CharField(default='pending', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='JobDetails',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('customer_name', models.CharField(default='narendrasir', max_length=128)),
                ('createdateTime', models.CharField(default='cat', max_length=128)),
                ('WantedDate', models.CharField(default='cat', max_length=128)),
                ('Wantedtimestart', models.CharField(default='cat', max_length=128)),
                ('category_name', models.CharField(default='cat', max_length=128)),
                ('subcategory_name', models.CharField(default='subc', max_length=128)),
                ('status', models.CharField(default='done/pending/canceled', max_length=128)),
                ('description', models.CharField(default='describe', max_length=128)),
            ],
        ),
    ]
