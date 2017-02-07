# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('role', models.TextField()),
                ('user', models.OneToOneField(related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('members_to_projects', models.ManyToManyField(related_name='projects_to_members', to='the_hub_site.Member', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(default=2017, choices=[(2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)])),
                ('season', models.CharField(max_length=50)),
                ('members_to_semesters', models.ManyToManyField(related_name='semesters_to_members', to='the_hub_site.Member', blank=True)),
            ],
            options={
                'ordering': ('-year',),
            },
        ),
        migrations.AddField(
            model_name='projects',
            name='semester',
            field=models.ForeignKey(related_name='projects_to_semester', to='the_hub_site.Semester'),
        ),
    ]
