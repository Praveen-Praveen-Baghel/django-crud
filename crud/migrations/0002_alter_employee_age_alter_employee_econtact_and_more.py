# Generated by Django 4.2.6 on 2023-10-31 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='employee',
            name='econtact',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='passout',
            field=models.IntegerField(max_length=4),
        ),
    ]
