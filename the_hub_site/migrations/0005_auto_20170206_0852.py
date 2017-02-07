# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_hub_site', '0004_auto_20170206_0749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='semester_to_projects',
        ),
        migrations.AddField(
            model_name='semester',
            name='projects_to_semester',
            field=models.ManyToManyField(related_name='semester_to_projects', to='the_hub_site.Projects', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
