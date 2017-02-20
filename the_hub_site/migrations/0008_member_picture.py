# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_hub_site', '0007_auto_20170207_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='picture',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
    ]
