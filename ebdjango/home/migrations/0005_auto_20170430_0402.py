# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-30 04:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170430_0239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='user',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='userwishlist',
            old_name='user',
            new_name='username',
        ),
    ]
