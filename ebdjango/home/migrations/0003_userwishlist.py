# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_users_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(default='', max_length=100)),
            ],
        ),
    ]