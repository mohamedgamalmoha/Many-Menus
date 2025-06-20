# Generated by Django 5.1.4 on 2025-06-14 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0012_alter_socialmedia_platform'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='maininfo',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='maininfo',
            name='title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='service',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='service',
            name='title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='theme',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='theme',
            name='title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Title'),
        ),
    ]
