# Generated by Django 4.2.9 on 2024-05-14 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0003_remove_account_id_alter_account_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('Date', models.DateField()),
                ('Time', models.CharField(max_length=20)),
                ('people', models.IntegerField(max_length=2)),
                ('space', models.CharField(max_length=1)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.account')),
            ],
        ),
    ]
