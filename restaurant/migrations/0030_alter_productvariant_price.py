# Generated by Django 5.1.4 on 2025-02-12 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0029_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='price',
            field=models.CharField(max_length=50, verbose_name='Variant Price'),
        ),
    ]
