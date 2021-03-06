# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-09 15:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CMSMetaTags',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cmsmetatags_cmsmetatags', serialize=False, to='cms.CMSPlugin')),
                ('meta_title', models.CharField(blank=True, default='', help_text='shown as browser tab title, defaults to page->settings->title', max_length=255, verbose_name='Page title')),
                ('meta_description', models.TextField(blank=True, default='', help_text='SEO descriptiomn, defaults to page->settings->meta description', max_length=355, verbose_name='Meta description')),
                ('fb_type', models.CharField(blank=True, default='website', max_length=255, verbose_name='Facebook Type')),
                ('fb_title', models.CharField(blank=True, default='', max_length=255, verbose_name='Facebook title')),
                ('fb_description', models.TextField(blank=True, default='', max_length=355, verbose_name='Facebook description')),
                ('fb_appid', models.CharField(blank=True, default='', max_length=255, verbose_name='Facebook app id')),
                ('fb_image', filer.fields.image.FilerImageField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL, verbose_name='Facebook image')),
            ],
            options={
                'verbose_name': 'Meta tags',
                'verbose_name_plural': 'Meta tags',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
