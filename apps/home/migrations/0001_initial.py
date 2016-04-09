# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('author', models.CharField(max_length=200, verbose_name='Author')),
                ('publish_date', models.DateField(max_length=255, verbose_name='Published date')),
                ('image', models.ImageField(upload_to='heros/', verbose_name='Hero image..')),
                ('addtional_image', models.ImageField(upload_to='additional/', null=True, verbose_name='Additional image', blank=True)),
                ('content', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Article..',
                'verbose_name_plural': 'Articles..',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=255, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Article category..',
                'verbose_name_plural': 'Article categories.',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='home.Category'),
            preserve_default=True,
        ),
    ]
