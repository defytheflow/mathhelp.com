# Generated by Django 3.0.5 on 2020-04-20 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_auto_20200405_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='filename',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]