# Generated by Django 4.2.9 on 2024-06-17 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0011_alter_reservations_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='id',
            field=models.CharField(default='527813436G', max_length=10, primary_key=True, serialize=False),
        ),
    ]
