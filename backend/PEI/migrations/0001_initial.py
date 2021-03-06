# Generated by Django 4.0.3 on 2022-06-09 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='img/')),
                ('title', models.TextField()),
                ('price', models.IntegerField()),
                ('brand', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter', models.TextField()),
                ('value', models.TextField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PEI.product')),
            ],
        ),
        migrations.AddConstraint(
            model_name='parameter',
            constraint=models.UniqueConstraint(fields=('id', 'parameter'), name='parameter_for_product'),
        ),
    ]
