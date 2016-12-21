# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_remove_noticia_data_hora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='autor',
        ),
    ]
