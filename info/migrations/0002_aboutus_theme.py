# Generated by Django 4.2.17 on 2024-12-11 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('title_en', models.CharField(max_length=500, null=True, verbose_name='Title')),
                ('title_ar', models.CharField(max_length=500, null=True, verbose_name='Title')),
                ('title_he', models.CharField(max_length=500, null=True, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_en', models.TextField(null=True, verbose_name='Description')),
                ('description_ar', models.TextField(null=True, verbose_name='Description')),
                ('description_he', models.TextField(null=True, verbose_name='Description')),
                ('image', models.ImageField(upload_to='about_us/', verbose_name='Image')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create At')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update At')),
            ],
            options={
                'verbose_name': 'About Us',
                'verbose_name_plural': 'About Us',
                'ordering': ('-create_at', '-update_at'),
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('title_en', models.CharField(max_length=500, null=True, verbose_name='Title')),
                ('title_ar', models.CharField(max_length=500, null=True, verbose_name='Title')),
                ('title_he', models.CharField(max_length=500, null=True, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_en', models.TextField(null=True, verbose_name='Description')),
                ('description_ar', models.TextField(null=True, verbose_name='Description')),
                ('description_he', models.TextField(null=True, verbose_name='Description')),
                ('image', models.ImageField(upload_to='theme/', verbose_name='Image')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create At')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update At')),
            ],
            options={
                'verbose_name': 'Theme',
                'verbose_name_plural': 'Themes',
                'ordering': ('-create_at', '-update_at'),
            },
        ),
    ]
