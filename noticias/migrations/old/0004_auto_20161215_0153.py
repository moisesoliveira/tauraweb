# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_remove_noticia_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='titulo',
            field=models.TextField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='texto',
            field=models.TextField(max_length=3096),
        ),
    ]
