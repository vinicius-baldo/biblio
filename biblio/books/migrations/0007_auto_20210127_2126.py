# Generated by Django 3.1.5 on 2021-01-28 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20210125_2320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='data_pub',
            new_name='data_reserva',
        ),
    ]