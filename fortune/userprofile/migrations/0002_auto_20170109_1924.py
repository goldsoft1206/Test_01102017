# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-09 19:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='randome_number',
            new_name='random_number',
        ),
    ]
