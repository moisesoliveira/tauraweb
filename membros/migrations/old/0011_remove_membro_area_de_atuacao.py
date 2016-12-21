# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0010_remove_membro_joined_up'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membro',
            name='area_de_atuacao',
        ),
    ]
