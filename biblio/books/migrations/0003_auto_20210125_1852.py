# Generated by Django 3.1.5 on 2021-01-25 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_books_data_atualizacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='data_pub',
            field=models.DateField(verbose_name='data da publicacao'),
        ),
    ]
