# Generated by Django 4.0.3 on 2022-06-09 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PEI', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='model',
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.TextField(default='generic'),
        ),
    ]
