# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('categoryName', models.CharField(default='category', max_length=128)),
                ('subcategoryName', models.CharField(default='subcategory', max_length=128)),
            ],
        ),
    ]
