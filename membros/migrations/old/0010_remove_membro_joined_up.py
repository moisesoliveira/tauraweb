# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0009_auto_20161215_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membro',
            name='joined_up',
        ),
    ]
