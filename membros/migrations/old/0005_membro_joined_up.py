# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0004_membro_area_de_atuacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='membro',
            name='joined_up',
            field=models.DateField(default=1, auto_now=True),
            preserve_default=False,
        ),
    ]
