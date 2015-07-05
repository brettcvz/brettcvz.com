# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('tagline', models.CharField(max_length=255)),
                ('image', models.URLField()),
                ('pubdate', models.DateField(auto_now_add=True)),
                ('visible', models.BooleanField(default=True)),
                ('content', models.TextField()),
                ('on_front_page', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-pubdate'],
            },
            bases=(models.Model,),
        ),
    ]
