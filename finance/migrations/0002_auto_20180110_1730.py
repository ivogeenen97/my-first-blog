# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-10 16:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('catogory', models.CharField(choices=[('Food', 'Food'), ('Social life', 'Social life'), ('Transportation', 'Transportation'), ('Household', 'Household'), ('Culture', 'Culture'), ('Other', 'Other')], max_length=100)),
                ('amount', models.FloatField()),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='income',
            name='amount',
            field=models.FloatField(),
        ),
    ]