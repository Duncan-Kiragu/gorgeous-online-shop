# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 10:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20171112_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_number_name', models.CharField(max_length=40)),
                ('street', models.CharField(max_length=40)),
                ('town', models.CharField(max_length=40)),
                ('postcode', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliveryAddresses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]