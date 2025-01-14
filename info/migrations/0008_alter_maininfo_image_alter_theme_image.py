# Generated by Django 4.2.17 on 2025-01-14 19:48

from django.db import migrations
import django_resized.forms
import restaurant.validators


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_socialmedia_theme_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininfo',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='home/', validators=[restaurant.validators.FileSizeValidator(max_upload_file_size=20971520)], verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1080, 1920], upload_to='themes/', validators=[restaurant.validators.FileSizeValidator(max_upload_file_size=20971520)], verbose_name='Image'),
        ),
    ]
