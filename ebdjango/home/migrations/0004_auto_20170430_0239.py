# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-30 02:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20170430_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_wishes', to=settings.AUTH_USER_MODEL),
        ),
    ]
