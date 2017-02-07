# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_hub_site', '0002_auto_20170205_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='user',
        ),
    ]
