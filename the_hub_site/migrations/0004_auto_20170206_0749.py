# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_hub_site', '0003_remove_member_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='semester',
        ),
        migrations.AddField(
            model_name='projects',
            name='semester_to_projects',
            field=models.ManyToManyField(related_name='projects_to_semester', to='the_hub_site.Semester', blank=True),
        ),
    ]
