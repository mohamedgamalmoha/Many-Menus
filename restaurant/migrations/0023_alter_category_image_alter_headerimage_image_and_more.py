# Generated by Django 4.2.17 on 2024-12-23 09:32

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0022_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, null=True, quality=80, scale=None, size=[300, 300], upload_to='categories/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='headerimage',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, null=True, quality=90, scale=None, size=[1920, 1080], upload_to='headers/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=85, scale=None, size=[600, 600], upload_to='products/', verbose_name='Product Image'),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='icon',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=50, scale=None, size=[50, 50], upload_to='icons/', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, null=True, quality=80, scale=None, size=[150, 150], upload_to='restaurants/', verbose_name='Image'),
        ),
    ]
