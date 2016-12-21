# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0003_remove_membro_matricula'),
    ]

    operations = [
        migrations.AddField(
            model_name='membro',
            name='area_de_atuacao',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
