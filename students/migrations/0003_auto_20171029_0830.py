# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-29 03:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20171022_2247'),
    ]

    operations = [
		
        migrations.AlterField(
            model_name='marks',
            name='suser_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student'),
        ),
        migrations.AddField(
            model_name='marks',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='marks',
            unique_together=set([('suser_name', 'sub_id')]),
        ),
    ]
