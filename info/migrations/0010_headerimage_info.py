# Generated by Django 5.1.4 on 2025-01-26 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_headerimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerimage',
            name='info',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='header_images', to='info.maininfo', verbose_name='Header Image'),
        ),
    ]
