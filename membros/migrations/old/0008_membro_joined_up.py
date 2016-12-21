# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0007_remove_membro_joined_up'),
    ]

    operations = [
        migrations.AddField(
            model_name='membro',
            name='joined_up',
            field=models.DateField(default=1, auto_now=True),
            preserve_default=False,
        ),
    ]
