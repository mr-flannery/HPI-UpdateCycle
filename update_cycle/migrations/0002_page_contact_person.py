# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('update_cycle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='contact_person',
            field=models.CharField(default='Frank Wittmann', max_length=200),
            preserve_default=False,
        ),
    ]
