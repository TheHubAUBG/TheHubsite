# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_hub_site', '0005_auto_20170206_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70)),
                ('type', models.CharField(default=b'presentation', max_length=14, choices=[(b'field_trip', b'Field Trip'), (b'presentation', b'Presentation'), (b'workshop', b'Workshop')])),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=300)),
                ('presenters', models.CharField(max_length=150)),
                ('level', models.CharField(default=b'beginner', max_length=14, choices=[(b'beginner', b'Beginner'), (b'intermediate', b'Intermediate'), (b'advanced', b'Advanced')])),
                ('target_audience', models.CharField(max_length=300)),
            ],
        ),
    ]
