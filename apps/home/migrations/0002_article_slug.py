# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='hssssswwwwwyyyy', populate_from='name', editable=False),
            preserve_default=False,
        ),
    ]
