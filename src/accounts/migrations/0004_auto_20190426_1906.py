# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-26 19:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190425_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 26, 19, 6, 44, 765261, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 26, 19, 6, 44, 765334, tzinfo=utc)),
        ),
    ]
