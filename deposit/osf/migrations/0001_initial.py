# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-28 11:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deposit', '0010_email_on_preferences'),
    ]

    operations = [
        migrations.CreateModel(
            name='OSFDepositPreferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_behalf_of', models.CharField(blank=True, help_text='If set, deposits will be associated to this OSF account.', max_length=128, null=True, verbose_name='OSF username')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deposit.Repository')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
