# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0008_membro_joined_up'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='joined_up',
            field=models.DateField(),
        ),
    ]
