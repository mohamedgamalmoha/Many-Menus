# Generated by Django 5.1.4 on 2025-01-26 09:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_headerimage_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='social_media_links', to='info.maininfo', verbose_name='Website Main Info'),
        ),
        migrations.AlterField(
            model_name='headerimage',
            name='info',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='header_images', to='info.maininfo', verbose_name='Website Main Info'),
        ),
    ]
