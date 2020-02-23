# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-26 21:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20190426_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 26, 21, 9, 28, 327315, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 26, 21, 9, 28, 327375, tzinfo=utc)),
        ),
    ]