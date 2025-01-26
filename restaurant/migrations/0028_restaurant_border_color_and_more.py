# Generated by Django 5.1.4 on 2025-01-26 09:39

import restaurant.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0027_alter_category_image_alter_headerimage_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='border_color',
            field=models.CharField(help_text='Border color for template (e.g., #RRGGBB or #RGB).', max_length=7, null=True, validators=[restaurant.validators.validate_hex_color], verbose_name='Border Color'),
        ),
        migrations.AlterField(
            model_name='socialmedialink',
            name='platform',
            field=models.CharField(choices=[('facebook', 'Facebook'), ('twitter', 'Twitter'), ('instagram', 'Instagram'), ('linkedin', 'LinkedIn'), ('tiktok', 'TikTok'), ('youtube', 'YouTube'), ('pinterest', 'Pinterest'), ('phone_number_1', 'Phone Number 1'), ('phone_number_2', 'Phone Number 2')], max_length=20, verbose_name='Platform'),
        ),
    ]
