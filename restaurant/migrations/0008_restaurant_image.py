# Generated by Django 4.2.16 on 2024-12-07 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_category_image_producttype_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(null=True, upload_to='restaurants/', verbose_name='Image'),
        ),
    ]
