# Generated by Django 4.2.9 on 2024-05-15 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_alter_reservations_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='Date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='id',
            field=models.CharField(default='1E06C30868', max_length=10, primary_key=True, serialize=False),
        ),
    ]
