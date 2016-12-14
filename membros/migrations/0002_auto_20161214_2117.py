# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membro',
            old_name='marticula',
            new_name='matricula',
        ),
    ]
