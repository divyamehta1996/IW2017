# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 19:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_userwishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='user',
            new_name='username',
        ),
    ]